#  Automated Metadata Generation System

This project is a web-based application that automatically extracts and generates metadata from uploaded documents (PDF, DOCX, TXT). It enhances document discoverability by summarizing content and identifying keywords using NLP techniques.

## 🚀 Features
- Upload support for `.pdf`, `.docx`, and `.txt`
- Text extraction from documents
- Semantic metadata generation using NLP:
  - Summary
  - Top keywords
  - Word count
- Download metadata as JSON
- Simple and clean web interface using Streamlit

## 🛠 Tech Stack
- Python
- Streamlit (for UI)
- PyMuPDF (for PDF text extraction)
- python-docx (for DOCX files)
- pytesseract, textract (for OCR/text extraction)
- spaCy + KeyBERT (for NLP/keywords/summary)

## 🧪 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/automated-metadata-generator.git
cd automated-metadata-generator
```

### 2. Set up a virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate    # on Windows
# or
source venv/bin/activate   # on Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the spaCy English model
```bash
python -m spacy download en_core_web_sm
```

### 5. Run the Streamlit app
```bash
streamlit run app.py
```

## 📦 Output Example
```json
{
  "word_count": 241,
  "summary": "This is an example summary of the first few sentences.",
  "keywords": ["metadata", "document", "semantic"]
}
```

## 📹 Demo Video
Include a short demo of the app in action.
The files used in the video are 
"23115022 Arkaprava Biswas Declaration form.pdf" is used to demonstrate metadata generation for pdf files.
"requirements.txt" is used as a text file to demonstrate metadata generation for pdf files.
"23115022 Arkaprava Biswas Declaration form.docx"  is used as a word file to demonstrate metadata generation for word files.
## 🤝 Contribution
Pull requests are welcome. For major changes, please open an issue first.


