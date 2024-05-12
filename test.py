'''import transformers
from transformers import AutoTokenizer,AutoModelForSeq2SeqLM,pipeline
import os
import torch
print(torch.cuda.is_available())
# Load the pre-trained model and tokenizer

token_name = "models/tokenizer"
model_name = "models/pegasus-lease-model"
tokenizer = AutoTokenizer.from_pretrained(token_name)
input_text = "fantastic apartment oasis in the heart of san diego great restaurants attractions museums shopping bars and more right at your door this modern studio is well furnished with lots of natural lights whether you are a solo traveler a couple or coming with friends and family you ll love this relaxing oasis in downtown san diego walking distance to the ocean seaport village gaslamp district convention center museums train stop restaurants cafes shops sign up with this link to get off your first airbnb trip only applies for new users the bedroom features a queen size bed and is isolated from a living room which creates a feeling like this is one bedroom apartment living room has a big sofa that doesn t turn into a bed but one person can sleep on it dining table with chairs kitchen is really functional has everything you need fridge stove dishwasher garbage disposal toaster microwave kettle coffee maker dis sign up with this link to get off your first airbnb trip only applies for new users the bedroom features a queen size bed and is isolated from a living room which creates a feeling like this is one bedroom apartment living room has a big sofa that doesn t turn into a bed but one person can sleep on it dining table with chairs kitchen is really functional has everything you need fridge stove dishwasher garbage disposal toaster microwave kettle coffee maker dishes pots and pans and views of a sunny courtyard kitchen is stocked up with coffee tea sugar paper towels cups glasses also there is a small balcony patio with a view of courtyard and little bit of downtown ac wifi internet tv with roku device i will provide you with netflix and sling spacious bathroom an additional air mattress two can sleep building amenities that you will have access to assigned indoor parking space rooftop pool with views of downtown and ocean jacuzzi h fitness gym laundry room please be familiar with airbnb terms conditions as well as the house rules in order to maximize the enjoyment of your stay please be respectful of my home neighbors and community you will be charged and or lose your full deposit is any of the following house rules are broken there is a zero tolerance policy with noise complaints no parties or events no pets no smoking inside on the balcony or in or out front of the building disrespecting the neighbors contacting property management staff or on site employees we are your point of contact and will address and fix any and all issues parking in the wrong spot there is no parking for guests any vehicles parked in unauthorized spaces and or not displaying the proper permit will be towed at the owner s expense not following check in and check out instructions staying past check out time unless prior written approval in airbnb messages have more guests than stated in your reservation no additional overnight guests without pre authorization loud music any disturbance especially noise past pm quiet hours"

# Tokenize the input text
input_ids = tokenizer(input_text, return_tensors="pt")["input_ids"]
device = 'cpu'
model = AutoModelForSeq2SeqLM.from_pretrained(model_name,use_safetensors=True)
gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 256}
pipe = pipeline("summarization",model=model,tokenizer=tokenizer)
summary_text = pipe(input_text,**gen_kwargs)[0]['summary_text']
print(summary_text)'''
import firebase_admin
from firebase_admin import credentials,firestore
import spacy
nlp = spacy.load("en_core_web_sm")
cred = credentials.Certificate("lease-summarization-firebase-adminsdk-73zq4-49a66ec68b.json")
firebase_admin.initialize_app(cred)
text = """Page 1 of 7
California Standard Residential Lease Agreement
LANDLORD _____________________________________
TENANT(S) _____________________________________
_____________________________________
PROPERTY ADDRESS: _____________________________________
_____________________________________
I. Lease Length Duration: The premises are leased on the following lease term: 
(please check one item only) 
☐ Month-to-Month 
(or)
☐ Until ________________, 20 ____. 
II. Rental Amount: Beginning ________________, 20____ TENANT agrees to pay 
LANDLORD the sum of $________________ per month in advance on the ____ day 
of each calendar month. Said rental payment shall be delivered by TENANT to 
LANDLORD or his designated agent to the following location: 
_____________________________________________________. Rent must be 
actually received by LANDLORD, or designated agent, in order to be considered in 
compliance with the terms of this agreement. 
III. Initial Payment: TENANT shall pay the first month rent of $________________ and 
the security deposit in the amount of $________________ for a total of 
$________________. Said payment shall be made in the form of cash or cashier's 
check and is all due prior to occupancy. 
IV. Security Deposits: TENANT shall deposit with landlord the sum of 
$________________ as a security deposit to secure TENANT'S faithful performance 
of the terms of this lease. The security deposit shall not exceed two times the monthly 
rent. After all the TENANTS have left, leaving the premises vacant, the LANDLORD 
may use the security deposit for the cleaning of the premises, any unusual wear and 
tear to the premises or common areas, and any rent or other amounts owed pursuant 
to the lease agreement or pursuant to Civil Code Section 1950.5. TENANT may not 
use said deposit for rent owed during the term of the lease. Within 21 days of the 
TENANT vacating the premises, LANDLORD shall furnish TENANT a written 
statement indicating any amounts deducted from the security deposit and returning the 
balance to the TENANT. If TENANT fails to furnish a forwarding address to 
LANDLORD, then LANDLORD shall send said statement and any security deposit 
refund to the leased premises. 
Page 2 of 7
V. Utilities: TENANT shall pay for all utilities and/or services supplied to the premises 
with the following exception: 
_____________________________________________________________________
____________________________________________________________________. 
VI. Occupants: The premises shall not be occupied by any person other than those 
designated above as TENANT with the exception of the following named persons:
_____________________________________________________________________
____________________________________________________________________.
If LANDLORD, with written consent, allows for additional persons to occupy the 
premises, the rent shall be increased by $________________ for each such person. 
Any person staying 14 days cumulative or longer, without the LANDLORD'S written 
consent, shall be considered as occupying the premises in violation of this agreement. 
VII. Subletting or Assigning: TENANT agrees not to assign or sublet the premises or any 
part thereof, without first obtaining written permission from LANDLORD. 
VIII. Parking: TENANT ☐ is not ☐ is (check one) assigned a parking space. If assigned a 
parking space it shall be designated as space #________________ TENANT may 
only park a vehicle that is registered in the TENANT'S name. 
TENANT may not assign, sublet, or allow any other person to use this space. The 
TENANT uses this space exclusively for parking of passenger automobiles. No other 
type of vehicle or item may be stored in this space without prior written consent of 
LANDLORD. TENANT may not wash, repair, or paint in this space or at any other 
common area on the premises. Only vehicles that are operational and currently 
registered in the State of California may park in this space. Any vehicle that is leaking 
any substance must not be parked anywhere on the premises. 
IX. Condition of Premises: TENANT acknowledges that the premises have been 
inspected. Tenant acknowledges that said premises have been cleaned and all items, 
fixtures, appliances, and appurtenances are in complete working order. TENANT 
promises to keep the premises in a neat and sanitary condition and to immediately 
reimburse landlord for any sums necessary to repair any item, fixture or appurtenance 
that needed service due to TENANT'S, or TENANT'S invitee, misuse or negligence. 
☐ TENANT shall be responsible for the cleaning or repair to any plumbing fixture 
where a stoppage has occurred. 
☐ TENANT shall also be responsible for repair or replacement of the garbage disposal 
where the cause has been a result of bones, grease, pits, or any other item that 
normally causes blockage of the mechanism. 
X. Alterations: TENANT shall not make any alterations to the premises, including but not 
limited to installing aerials, lighting fixtures, dishwashers, washing machines, dryers or 
other items without first obtaining written permission from LANDLORD. TENANT shall 
not change or install locks, paint, or wallpaper said premises without LANDLORD'S 
Page 3 of 7
prior written consent, TENANT shall not place placards, signs, or other exhibits in a 
window or any other place where they can be viewed by other residents or by the 
general public. 
XI. Late Charge/Bad Checks: A late charge of 6% of the current rental amount shall be 
incurred if rent is not paid when due. If rent is not paid when due and landlord issues a 
'Notice to Pay Rent or Quit', TENANT must tender cash or cashier's check only. If 
TENANT tenders a check, which is dishonored by a banking institution, than TENANT 
shall only tender cash or cashier's check for all future payments. This shall continue 
until such time as written consent is obtained from LANDLORD. In addition, TENANT 
shall be liable in the sum of $____ for each check that is returned to LANDLORD 
because the check has been dishonored. 
XII. Noise and Disruptive Activities: TENANT or his/her guests and invitees shall not 
disturb, annoy, endanger or inconvenience other tenants of the building, neighbors, 
the LANDLORD or his agents, or workmen nor violate any law, nor commit or permit 
waste or nuisance in or about the premises. Further, TENANT shall not do or keep 
anything in or about the premises that will obstruct the public spaces available to other 
residents. Lounging or unnecessary loitering on the front steps, public balconies or the 
common hallways that interferes with the convenience of other residents is prohibited. 
XIII. Landlord's Right of Entry: LANDLORD may enter and inspect the premises during 
normal business hours and upon reasonable advance notice of at least 24 hours to 
TENANT. LANDLORD is permitted to make all alterations, repairs and maintenance 
that in LANDLORD'S judgment is necessary to perform. In addition LANDLORD has 
all right to enter pursuant to Civil Code Section 1954. If the work performed requires 
that TENANT temporarily vacate the unit, then TENANT shall vacate for this temporary 
period upon being served a 7 days notice by LANDLORD. TENANT agrees that in 
such event that TENANT will be solely compensated by a corresponding reduction in 
rent for those many days that TENANT was temporarily displaced. 
If the work to be performed requires the cooperation of TENANT to perform certain 
tasks, then those tasks shall be performed upon serving 24 hours written notice by 
LANDLORD. (EXAMPLE -removing food items from cabinets so that the unit may be 
sprayed for pests) 
XIV. Repairs by Landlord: Where a repair is the responsibility of the LANDLORD,
TENANT must notify LANDLORD with a written notice stating what item needs 
servicing or repair. TENANT must give LANDLORD a reasonable opportunity to 
service or repair said item. TENANT acknowledges that rent will not be withheld 
unless a written notice has been served on LANDLORD giving LANDLORD a 
reasonable time to fix said item within the meaning of Civil Code Section 1942. Under 
no circumstances may TENANT withhold rent unless said item constitutes a 
substantial breach of the warrantee of habitability as stated in Code of Civil Procedure 
Section 1174.2. 
 
XV. Pets: No dog, cat, bird, fish or other domestic pet or animal of any kind may be kept 
on or about the premises without LANDLORD"S written consent. 
Page 4 of 7
XVI. Furnishings: No liquid filled furniture of any kind may be kept on the premises. If the 
structure was built in 1973 or later TENANT may possess a waterbed if he maintains 
waterbed insurance valued at $100,000 or more. TENANT must furnish LANDLORD 
with proof of said insurance. TENANT must use bedding that complies with the load 
capacity of the manufacturer. In addition, TENANT must also be in full compliance with 
Civil Code Section 1940.5. 
☐ TENANT shall not install or use any washer, dryer, or dishwasher that was not 
already furnished with the unit. 
XVII. Insurance: TENANT may maintain a personal property insurance policy to cover any 
losses sustained to TENANT'S personal property or vehicle. It is acknowledged that 
LANDLORD does not maintain this insurance to cover personal property damage or 
loss caused by fire, theft, rain, water overflow/leakage, acts of GOD, and/or any other 
causes. 
It is acknowledged that LANDLORD is not liable for these occurrences. It is 
acknowledged that TENANT'S insurance policy shall solely indemnify TENANT for any 
losses sustained. TENANT'S failure to maintain said policy shall be a complete waiver 
of TENANT'S right to seek damages against LANDLORD for the above stated losses. 
The parties acknowledge that the premises are not to be considered a security 
building which would hold LANDLORD to a higher degree of care. 
XVIII. Termination of Lease/Rental Agreement: If this lease is based on a fixed term, 
pursuant to paragraph 2, then at the expiration of said fixed term this lease shall 
become a month to month tenancy upon the approval of LANDLORD. Where said 
term is a month to month tenancy, either party may terminate this tenancy by the 
serving of a 30-day written notice. 
XIX. Possession: If premises cannot be delivered to TENANT on the agreed date due to 
loss, total or partial destruction of the premises, or failure of previous TENANT to 
vacate, either party may terminate this agreement upon written notice to the other 
party at their last known address. It is acknowledged that either party shall have no 
liability to each other except that all sums paid to LANDLORD will be immediately 
refunded to TENANT. 
XX. Abandonment: It shall be deemed a reasonable belief by the LANDLORD that an 
abandonment of the premises has occurred where the, within the meaning of Civil 
Code Section 1951.2, where rent has been unpaid for 14 consecutive days and the 
TENANT has been absent from unit for 14 consecutive days. In that event, 
LANDLORD may serve written notice pursuant to Civil Code Section 1951.2. If 
TENANT does not comply with the requirements of said notice in 18 days, the 
premises shall be deemed abandoned. 
XXI. Waiver: LANDLORD'S failure to require compliance with the conditions of this 
agreement, or to exercise any right provided herein, shall not be deemed a waiver by 
LANDLORD of such condition or right. LANDLORD'S acceptance of rent with 
knowledge of any default under agreement by TENANT shall not be deemed a waiver 
Page 5 of 7
of such default, nor shall it limit LANDLORD'S rights with respect to that or any 
subsequent right. If is further agreed between the parties that the payment of rent at 
any time shall not be a waiver to any UNLAWFUL DETAINER action unless 
LANDLORD in writing specifically acknowledges that this constitutes a waiver to the 
UNLAWFUL DETAINER action. 
XXII. Validity/Severability: If any provision of this agreement is held to be invalid, such 
invalidity shall not affect the validity or enforceability of any other provision of this 
agreement. 
XXIII. Attorney Fees: In the event action is brought by any party to enforce any terms of this 
agreement or to recover possession of the premises, the prevailing party shall recover 
from the other party reasonable attorney fees. 
It is acknowledged, between the parties, that jury trials significantly increase the costs 
of any litigation between the parties. It is also acknowledged that jury trials require a 
longer length of time to adjudicate the controversy. On this basis, all parties waive their 
rights to have any matter settled by jury trial. 
XXIV. Notices: All notices to the tenant shall be deemed served upon mailing by first class 
mail, addressed to the tenant, at the subject premises or upon personal delivery to the 
premises whether or not TENANT is actually present at the time of said delivery. All 
notices to the landlord shall be served by mailing first class mail or by personal 
delivery to the manager's apartment or to: 
_____________________________________________________________________
____________________________________________________________________. 
XXV. Personal Property of Tenant: Once TENANT vacates the premises, the LANDLORD 
shall store all personal property left in the unit for 18 days. If within that time period, 
TENANT does not claim said property, LANDLORD may dispose of said items in any 
manner LANDLORD chooses. 
XXVI. Additional Rent: All items owed under this lease shall be deemed additional rent. 
XXVII. Application: All statements in TENANT'S application must be true or this will 
constitute a material breach of this lease. 
XXVIII. Governing Law: This Lease shall be governed by and construed in accordance 
with the laws of the State of California.
XXIX. Megan’s Law: Notice: Pursuant to Section 290.46 of the Penal Code, information 
about specified registered sex offenders is made available to the public via an Internet 
Web site maintained by the Department of Justice at www.meganslaw.ca.gov. 
Depending on an offender's criminal history, this information will include either the 
address at which the offender resides or the community of residence and ZIP Code in 
which he or she resides.
XXX. Additional Terms:
_____________________________________________________________________
Page 6 of 7
_____________________________________________________________________
_____________________________________________________________________
Notice: The California Department of Justice, sheriff’s departments, police 
departments serving jurisdictions of 200,000 or more and many other local law 
enforcement authorities maintain for public access a data base of the locations 
of persons required to register pursuant to paragraph (1) of subdivision (a) of 
Section 290.4 of the Penal Code. The database is updated on a quarterly basis 
and a source of information about the presence of these individuals in any 
neighborhood. The Department of Justice also maintains a Sex Offender 
Identification Line through which inquiries about individuals may be made. This 
is a "900" telephone service. Callers must have specific information about 
individuals they are checking. Information regarding neighborhoods is not 
available through the "900" telephone service. 
XXXI. Entire Agreement: The foregoing agreement, including any attachments incorporated 
by reference, constitute the entire agreement between the parties and supersedes any 
oral or written representations or agreements that may have been made by either 
party. Further, TENANT represents that TENANT has relied solely on TENANT'S 
judgment in entering into this agreement. TENANT acknowledges having been 
advised to consult with independent legal counsel before entering into this Agreement 
and has decided to waive such representation and advice. TENANT acknowledges 
that TENANT has read and understood this agreement and has been furnished a 
duplicate original. 
LANDLORD/AGENT’S SIGNATURE ________________________________
PRINTED NAME ______________________________ DATE ____________ 
TENANT’S SIGNATURE ________________________________
PRINTED NAME ______________________________ DATE ____________ 
TENANT’S SIGNATURE ________________________________
PRINTED NAME ______________________________ DATE ____________ 
Page 7 of 7
CALIFORNIA FLOOD DISCLOSURE
This Flood Disclosure Addendum is made part of the lease agreement dated 
_________________, 20____, by and between _________________ (“Landlord”) and 
_________________ (“Tenant”) for the property located at _________________, City of 
_________________, State of California. 
Per Section 8589.45 of the Government Code, the Landlord is required to provide any and all 
information if the rental property is at risk of flooding as deemed by the State of California.
The Landlord hereby discloses the following: (initial)
____ - The Landlord has NO KNOWLEDGE that the rental property is located in a special 
flood hazard area of an area at risk to potential flooding;
OR
____ - The Landlord IS AWARE and discloses to Tenant the rental property is located in a 
flood hazard area or an area that has a high risk to potential flooding. Under State law, the 
Landlord can declare they have actual knowledge of a flooding hazard on the rental property 
if one (1) of the following are true:
• The Landlord currently holds flood insurance on the rental property;
• The Landlord has received notice from a public, government, or equivalent agency that 
the rental property is located in a special flood hazard zone or an area of potential 
flooding; or
• The Landlord’s mortgage holder requires the Landlord to carry flood insurance.
The Tenant has the right to seek information about hazards, not limited to flooding, that may 
affect the rental property from the Office of Emergency Services at the web address of 
http://myhazards.caloes.ca.gov/.
It shall be known that the Landlord’s insurance does not cover the loss of the Tenant’s 
personal possessions or for any relocation expenses. Any losses would be the sole 
responsibility of the Tenant. Therefore, the Tenant should consider purchasing their own 
insurance to cover these items. The Landlord does not need to provide any additional 
information concerning the potential of flood hazards on the rental property.
The following parties have reviewed the information about and certify, to the best of their 
knowledge, that the information provided by the signatory is true and accurate.
LANDLORD/AGENT’S SIGNATURE ____________________________ DATE ___________ 
TENANT’S SIGNATURE ____________________________________ DATE ____________
TENANT’S SIGNATURE ____________________________________ DATE ____________"""
data = {}
db = firestore.client()
'''coll_ref = db.collection('glossary')
for doc in coll_ref.stream():
    #print(doc.id.lower())
    data[doc.id.lower()] = doc.to_dict()['definition']
print(data)
#print(text.split(' '))
print(data.keys())
for key in data.keys():
    if key in text:
        print(key)
'''
import json
coll_ref = db.collection('laws')
laws = {}
for doc in coll_ref.stream():
    laws[doc.id.lower()] = doc.to_dict()
#print(laws)
#print(laws.keys())
tenant_favor = []
tenant_against = []
for law_name,law_info in laws.items():
    #print(laws[law_name]['Keywords'])
    if any(keyword in text for keyword in law_info['Keywords']):
        if law_info['In Favor of Tenant']:
            tenant_favor.append(law_info)
        else:
            tenant_against.append(law_info)
query = coll_ref.where("Keywords", "array_contains", "rental amount").stream()
#print(tenant_against)
#print(tenant_favor)
l =  [{'Charges': {'California': 'Requires landlords to maintain rental units in a habitable condition.', 'New York': 'Requires landlords to maintain rental units in a habitable condition.'}, 'In Favor of Tenant': True, 'Description': 'Specifies minimum standards for rental property habitability.', 'Keywords': ['habitability standards', 'property conditions', 'possession'], 'Acts': ['California Civil Code Section 1941.1', 'New York Real Property Law Section 235-b']}, {'Charges': {'California': "Landlords must provide at least 24 hours' written notice before entering a rental unit, except in cases of emergency.", 'New York': 'Landlords must provide reasonable notice and may only enter a rental unit for specific reasons, such as repairs or inspections.'}, 'In Favor of Tenant': True, 'Description': 'Regulates when and how landlords can access rental units.', 'Keywords': ['landlord access', 'property access', 'emergency', 'repairs', 'inspection'], 'Acts': ['California Civil Code Section 1954', 'New York Real Property Law Section 235-e']}, {'Charges': {'California': 'Limits annual rent increases to a certain percentage and provides eviction protections for eligible rental units.', 'New York': 'Regulates rent increases and provides stabilization for eligible rental units in specified areas.'}, 'In Favor of Tenant': True, 'Description': 'Imposes limits on rent increases and provides eviction protections for tenants.', 'Keywords': ['rent control', 'eviction protections', 'rental amount'], 'Acts': ['California Assembly Bill 1482', 'New York Rent Stabilization Law']}, {'Charges': {'California': "30 days' notice for increases less than 10% of the lowest rent charged in the last 12 months; 60 days' notice for increases of 10% or more.", 'New York': "30 days' notice for month-to-month tenants; 90 days' notice for tenants with a lease term of one year or more."}, 'In Favor of Tenant': True, 'Description': 'Specifies the notice period landlords must provide tenants before increasing the rent.', 'Keywords': ['rent increase', 'notice period', 'amount'], 'Acts': ['California Civil Code Section 1946.2', 'New York Real Property Law Section 235-f']}, {'Charges': {'California': 'Landlords must accept at least one form of payment that is not cash, unless tenant requests cash payment.', 'New York': "Landlords must accept personal checks, cashier's checks, money orders, or electronic payments."}, 'In Favor of Tenant': True, 'Description': 'Specifies acceptable methods of rent payment.', 'Keywords': ['rent payment', 'payment methods', 'rental amount'], 'Acts': ['California Civil Code Section 1962', 'New York Real Property Law Section 235-h']}, {'Charges': {'California': 'If landlord fails to repair within a reasonable time, tenant may make repairs and deduct costs from rent.', 'New York': 'Tenant may withhold rent until repairs are made, or seek legal remedies.'}, 'In Favor of Tenant': True, 'Description': 'Grants tenants the right to request repairs for essential services.', 'Keywords': ['right to repair', 'repair requests', 'repair', 'maintenance'], 'Acts': ['California Civil Code Section 1941.1', 'New York Real Property Law Section 235-bb']}, {'Charges': {'California': "Two months' rent for unfurnished units; three months' rent for furnished units.", 'New York': "One month's rent for unfurnished units; two months' rent for furnished units."}, 'In Favor of Tenant': True, 'Description': 'Limits the maximum amount a landlord can charge as a security deposit.', 'Keywords': ['security deposit', 'deposit limits'], 'Acts': ['California Civil Code Section 1950.5', 'New York Real Property Law Section 7-103']}, {'Charges': {'California': "Landlords must return security deposits within 21 days of the tenant's move-out date, along with an itemized statement of deductions.", 'New York': "Landlords must return security deposits within a reasonable time after the tenant's move-out date, along with an itemized statement of deductions."}, 'In Favor of Tenant': True, 'Description': 'Specifies requirements for returning security deposits to tenants.', 'Keywords': ['security deposit return', 'deposit refund', 'security deposit'], 'Acts': ['California Civil Code Section 1950.5', 'New York Real Property Law Section 7-103']}, {'Charges': {'California': 'Prohibits landlords from harassing tenants through actions such as threats, interruptions of essential services, or unauthorized entry.', 'New York': 'Prohibits landlords from harassing tenants through actions such as threats, interruptions of essential services, or unauthorized entry.'}, 'In Favor of Tenant': True, 'Description': 'Protects tenants from harassment by landlords or their agents.', 'Keywords': ['tenant harassment', 'harassment protections', 'tenant'], 'Acts': ['California Civil Code Section 1940.2', 'New York Real Property Law Section 235-f']}, {'Charges': {'California': 'Allows tenants to withhold rent for repairs, terminate the lease for certain violations, or pursue legal action against landlords.', 'New York': 'Allows tenants to withhold rent for repairs, terminate the lease for certain violations, or pursue legal action against landlords.'}, 'In Favor of Tenant': True, 'Description': 'Provides tenants with legal remedies for addressing housing issues.', 'Keywords': ['tenant remedies', 'legal action', 'repairs', 'termination', 'housing issues', 'maintenance'], 'Acts': ['California Civil Code Section 1942', 'New York Real Property Law Section 235-bb']}, {'Charges': {'California': 'Landlords can only charge actual screening costs, and must provide itemized receipts upon request.', 'New York': 'Landlords can only charge actual screening costs, and must provide itemized receipts upon request.'}, 'In Favor of Tenant': True, 'Description': 'Regulates fees landlords can charge for tenant screening.', 'Keywords': ['screening fees', 'tenant', 'cost', 'charge'], 'Acts': ['California Civil Code Section 1950.6', 'New York Real Property Law Section 238-a']}]
p = json.dumps(l)
print(p)
favorable = json.dumps(favorable)
unfavorable = json.dumps(unfavorable)
print(favorable)
print(unfavorable)