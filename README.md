
# LeaseSum - A rental lease summarizer and Assistant

Welcome to the Legal Text Summarizer repository! This project provides a web-based application that allows users to upload legal documents and receive concise summaries. The application is designed to help individuals quickly understand the key points of lengthy and complex legal texts.

## Features

- Document Upload
- Automated Summary Generation
- Estimated Rent and Security Deposit
- Glossary Recommendation on Legal terms
- Laws Recommendation in favor or against Tenant
- User-Friendly Interface



## Tech Stack

**Client:** HTML, JavaScript, BootstrapCSS

**Server:** Python, FastAPI

**Database:** NoSQL, Google Firebase

**Machine Learning:** XgBoost, TFIDF Vectorizer

**LLM:** Hugging Face Transformers



## Appendix

### A. Folder Structure

This section describes the folder structure of the project:

```
legal-text-summarizer/
├── static/
│   ├── css/
│   │   └── styles.css       # Custom CSS styles
│   ├── js/
│   │   └── main.js          # Custom JavaScript
├── templates/
│   └── index.html           # Main HTML file
├── uploads/                 # Directory for uploaded files
├── app.py                   # Main application file
├── requirements.txt         # Python dependencies
├── package.json             # Frontend dependencies
└── README.md                # Project documentation
```

### B. API Endpoints

This section provides details about the API endpoints available in the application:

- **POST /uploadfile/**
  - Description: Endpoint to upload a legal document.
  - Parameters: `file` (multipart/form-data)
  - Response: JSON object containing the summary of the document.

### C. Customization

You can customize the typing animation and other elements of the application. Here’s how you can do it:

1. **Typing Animation**: Modify the strings and settings in the `Typed.js` initialization:

    ```javascript
    <script>
      var typed = new Typed('#typing-container',{
        strings: ["Analyze your lease documents...", "Generate a concise summary...", "Provide estimated rent...", "Get expected Security Deposit..."],
        typeSpeed: 50,
        loop: true
      })
    </script>
    ```

2. **CSS Styles**: Add your custom styles in `static/css/styles.css`:

    ```css
    body {
      font-family: Arial, sans-serif;
      background-color: #f8f9fa;
    }
    #typing-container {
      font-size: 24px;
      color: #343a40;
      margin-top: 20px;
    }
    ```

3. **HTML Template**: Modify the main HTML template `templates/index.html` to adjust the layout and content.

### D. Troubleshooting

This section provides solutions to common issues you might encounter:

- **Issue**: Libraries not loading properly.
  - **Solution**: Ensure that the URLs in your `<script>` and `<link>` tags are correct and accessible. You can also check your internet connection.

- **Issue**: Typed.js animation not working.
  - **Solution**: Make sure that the Typed.js script is included after the HTML element you are targeting is rendered. Also, check for any JavaScript errors in the console.

### E. References

For more information, you can refer to the following resources:

- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Typed.js Documentation](https://github.com/mattboldt/typed.js/)
- [Flask Documentation](https://flask.palletsprojects.com/en/latest/)
- [Python Package Index (PyPI)](https://pypi.org/)

---
## Installation

Follow these steps to get the Legal Text Summarizer application up and running on your local machine.

### Prerequisites

Ensure you have the following software installed on your system:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/legal-text-summarizer.git
cd legal-text-summarizer
```

### Set Up the Python Environment

1. **Create a virtual environment** (recommended) and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Install Python dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

### Configure Environment Variables

1. **Create a `.env` file** in the root directory and add the required environment variables. Refer to the [Environment Variables](#environment-variables) section for details.

    Example `.env` file:

    ```text
    SECRET_KEY=your_secret_key
    UPLOAD_FOLDER=uploads/
    ALLOWED_EXTENSIONS=txt,pdf,docx
    MAX_CONTENT_LENGTH=16777216
    ```

### Run the Application

1. **Run the FastAPI application**:

    ```bash
    uvicorn app:app --reload
    ```

    Replace `app:app` with the correct import path if your FastAPI app is located in a different file or has a different name.

2. Open your browser and navigate to `http://localhost:8000` to see the application in action.

### API Documentation

FastAPI automatically generates interactive API documentation. You can access it at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Troubleshooting

If you encounter issues during installation, check the following:

- Ensure all prerequisites are installed.
- Verify that the virtual environment is activated.
- Confirm that the `.env` file is properly configured and placed in the root directory.
- Check the console for error messages and resolve any missing dependencies or syntax errors.

### Additional Notes

- **Updating Dependencies**: If there are updates to the dependencies, you can update your local setup by running:
  
    ```bash
    pip install -r requirements.txt --upgrade
    ```

- **Deactivating the Virtual Environment**: Once you're done working on the project, you can deactivate the virtual environment with:

    ```bash
    deactivate
    ```

By following these instructions, you should be able to successfully set up and run the Legal Text Summarizer application on your local machine. If you have any issues, feel free to open an issue on this repository.

## License

[MIT](https://choosealicense.com/licenses/mit/)


## 🚀 About Me
I'm a ML enthusiast and working on several Projects including Tech stacks like MERN, AI, ML. 
I have recently graduated from California State University, Fullerton. 


## Authors

- [Shrinivas Patil](https://github.com/Shridat)


## Feedback

If you have any feedback, please reach out to us at pshrinivas264@gmail.com
