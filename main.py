from typing import Union
from fastapi import FastAPI, Request, UploadFile, File 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import tempfile
import PyPDF2
import spacy
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk import sent_tokenize
import re
import pickle
import numpy as np
import sklearn 
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import xgboost
from transformers import pipeline, set_seed, AutoTokenizer,AutoModelForSeq2SeqLM
import firebase_admin
from firebase_admin import credentials,firestore
import json

nlp = spacy.load("en_core_web_sm")
cred = credentials.Certificate("lease-summarization-firebase-adminsdk-73zq4-49a66ec68b.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

'''with open('models/stack_reg.pkl', 'rb') as f:
    stack_reg = pickle.load(f)'''
#stack_reg = pickle.load(open('E:\Final Project\models\stack_reg.sav', 'rb'))

def text_clean(text):
    corpus = []
    ps = PorterStemmer()
    text = re.sub(r"(?:\@|https?\://)\S+", "", text)
    text = re.sub(' +',' ',text)
    text = re.sub('[^a-zA-Z]',' ',text)
    text = text.lower()
    text = text.split()
    text = [ps.stem(words) for words in text if words not in stopwords.words('english')]
    text = " ".join(text)
    corpus.append(text)
    return corpus
    
   
def tfidf_vect(text):
    #word_2_vec = Word2Vec(words, vector_size=100,window=5, min_count=1, workers=4)
    tf = TfidfVectorizer(max_features=10000,stop_words='english',ngram_range=(1, 2),sublinear_tf=True)
    text = tf.fit_transform(text).toarray()
    if(text.shape[1]<10000):
        text = np.pad(text,((0,0),(0,10000-text.shape[1])))
    return text

def rev_predict(X):
    with open("models/xgb.pkl","rb") as file:
        model = pickle.load(file)
    pred = model.predict(X)
    return pred

def price_predict(X):
    with open("models/xgb_price.pkl","rb") as file:
        model = pickle.load(file)
    pred = model.predict(X)
    return pred

def split_text_into_chunks(text, chunk_size):
    chunks = []
    words = text.split()
    current_chunk = ""
    current_chunk_word_count = 0
    for word in words:
        current_chunk += word + " "
        current_chunk_word_count += 1
        if current_chunk_word_count >= chunk_size:
            chunks.append(current_chunk.strip())
            current_chunk = ""
            current_chunk_word_count = 0
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def get_summary(chunks):
    summaries = []
    for chunk in chunks:
        summary = generate_summary(chunk)
        summaries.append(summary)
    return summaries

def generate_summary(text):
    text = re.sub(r"(?:\@|https?\://)\S+", "", text)
    text = re.sub(' +',' ',text)
    text = re.sub('[^a-zA-Z0-9\s]',' ',text)
    text = text.lower()
    text = text.split()
    text = " ".join(text)
    token_name = "models/tokenizer"
    model_name = "models/pegasus-lease-model"
    tokenizer = AutoTokenizer.from_pretrained(token_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name,use_safetensors=True)
    input_ids = tokenizer(text, return_tensors="pt",max_length=1024,truncation=True,padding=True)["input_ids"]
    summary_ids = model.generate(input_ids, max_length=128, num_return_sequences=2,num_beams=5, repetition_penalty=2.0)
    summary_text = ""
    summary_text = tokenizer.decode(summary_ids[0],skip_special_tokens=True)
    summary_text = summary_text.replace('/([^.!?])(?=\s*$)/g', '$1.')
    '''for i in range(len(summary_ids)):
        summary_text += tokenizer.decode(summary_ids[i], skip_special_tokens=True)'''
    return summary_text

def get_glossary(summary):
    coll_ref = db.collection('glossary')
    glossary_data = {}
    matched_terms = {}
    for doc in coll_ref.stream():
        glossary_data[doc.id.lower()] = doc.to_dict()['definition']
    for key in glossary_data.keys():
        if key in summary:
            matched_terms[key] = glossary_data[key]
    return matched_terms,glossary_data

def legal_guidance(text):
    coll_ref = db.collection('laws')
    laws = {}
    for doc in coll_ref.stream():
        laws[doc.id.lower()] = doc.to_dict()
    tenant_favor = []
    tenant_against = []
    for law_name,law_info in laws.items():
        #print(laws[law_name]['Keywords'])
        if any(keyword in text for keyword in law_info['Keywords']):
            if law_info['In Favor of Tenant']:
                tenant_favor.append(law_info)
            else:
                tenant_against.append(law_info)
    return tenant_favor, tenant_against
    
#print(laws)
app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates = Jinja2Templates(directory="templates")
    
@app.get('/',response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get('/about')
async def about():
    return {"About : About Us"}

@app.post('/uploadfile/',response_class=HTMLResponse)
async def upload_file(request:Request,file: UploadFile = File(...)):
    try:
        contents = await file.read()
        #print(contents[:100])
        #text_data = contents.decode("utf-8",errors="replace")
        #print(text_data)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(contents)
        #document = fitz.open(temp_pdf.name)
        document = PyPDF2.PdfReader(temp_pdf.name)
        num_pages = len(document.pages)
        print(num_pages)
        text_data = ""
        html_content = ""
        for page_num in range(num_pages):
            page_object = document.pages[page_num]
            text_data += " "+page_object.extract_text()
            text_data += "\n"
            html_content += f"<div>Page {page_num + 1}</div>"
            html_content += f"<div>{text_data}</div>"
        corpus = text_clean(text_data)
        #print(corpus)
        vect = tfidf_vect(corpus)
        #print(vect.shape)
        rev_pred = round(rev_predict(vect)[0],2)
        #print(pred)
        prices = price_predict(vect)
        exp_rent = round(prices[0][0],0)
        exp_sd = round(prices[0][1],0)
        chunks  = split_text_into_chunks(text_data,512)
        print(chunks)
        #print(get_summary(chunks))
        #print(word_vect(tokens,w2v))
        #print(set(names))
        #print(set(orgs))
        summary = get_summary(chunks)
        summary = "".join(summary)
        summary = summary.capitalize()
        #print(summary)
        matched_terms,glossary_data = get_glossary(summary)
        #print(matched_terms)
        #print(glossary_data)
        favorable,unfavorable = legal_guidance(text_data)
        print(favorable)
        print(unfavorable)
        favorable = json.dumps(favorable)
        unfavorable = json.dumps(unfavorable)
        #print(get_glossary(summary))
        return templates.TemplateResponse("result.html", {
            "request":request,
            "filename": file.filename,
            "content_length": len(contents),
            "text": text_data,
            "pdf_content": html_content,
            "rev_pred":rev_pred,
            "exp_rent":exp_rent,
            "exp_sd":exp_sd,
            "summary":summary,
            "matched_terms": matched_terms,
            "glossary_data":glossary_data,
            "favor": favorable,
            "unfavor":unfavorable
        })
    finally:
        await file.close()
