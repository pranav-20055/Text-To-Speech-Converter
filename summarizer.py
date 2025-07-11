import fitz  # PyMuPDF
from transformers import pipeline
import pyttsx3

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def summarize_text(text, max_len=150):
    summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""
    for chunk in chunks:
        out = summarizer("summarize: " + chunk, max_length=max_len, min_length=30, do_sample=False)
        summary += out[0]['summary_text'] + " "
    return summary.strip()

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
