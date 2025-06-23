
import streamlit as st
import fitz  # PyMuPDF
import docx
import pytesseract
import textract
from keybert import KeyBERT
import spacy
import json
import os

# Load NLP models

nlp = spacy.load("en_core_web_sm")
kw_model = KeyBERT()

# Text extractor
def extract_text(file):
    ext = os.path.splitext(file.name)[1].lower()
    if ext == ".pdf":
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join([page.get_text() for page in doc])
    elif ext == ".docx":
        f = file.read()
        with open("temp.docx", "wb") as out:
            out.write(f)
        doc = docx.Document("temp.docx")
        return "\n".join([para.text for para in doc.paragraphs])
    elif ext == ".txt":
        return file.read().decode("utf-8")
    else:
        return textract.process(file).decode("utf-8")

# Metadata generator
def generate_metadata(text):
    doc = nlp(text)
    keywords = kw_model.extract_keywords(text, stop_words='english', top_n=5)
    return {
        "word_count": len(text.split()),
        "summary": " ".join([sent.text for sent in list(doc.sents)[:3]]),
        "keywords": [kw[0] for kw in keywords]
    }

# Streamlit UI
st.set_page_config(page_title="Automated Metadata Generator", layout="centered")
st.title("📄 Automated Metadata Generator")

uploaded_file = st.file_uploader("Upload a document (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])
if uploaded_file:
    with st.spinner("Extracting content and generating metadata..."):
        try:
            text = extract_text(uploaded_file)
            metadata = generate_metadata(text)
            st.subheader("📌 Generated Metadata")
            st.json(metadata)

            st.download_button("Download Metadata as JSON", json.dumps(metadata), file_name="metadata.json")

        except Exception as e:
            st.error(f"Error: {e}")
