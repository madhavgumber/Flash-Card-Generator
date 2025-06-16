import streamlit as st
from openai import OpenAI
import pandas as pd
from PyPDF2 import PdfReader

# Initialize OpenAI client (this replaces openai.api_key = ...)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Flash Card Generator")
st.title("📚 Flash Card Generator using LLMs")
st.write("Upload text or PDF files and generate Q&A flashcards automatically.")

uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["pdf", "txt"])
manual_input = st.text_area("Or paste text below", height=200)

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""

if uploaded_file:
    text = extract_text(uploaded_file)
elif manual_input:
    text = manual_input
else:
    text = ""

def generate_flashcards(text, subject="General"):
    prompt = f"""
You are a helpful assistant that creates study flashcards.
Generate 10–15 question-answer flashcards from the following {subject} content:

{text[:3000]}

Use this format:
Q: ...
A: ...
Only return the flashcards.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content

if st.button("Generate Flashcards") and text:
    with st.spinner("Generating flashcards..."):
        output = generate_flashcards(text)
        flashcards = [line.strip() for line in output.split("\n") if line.strip()]
        
        questions, answers = [], []
        for i in range(0, len(flashcards), 2):
            if i+1 < len(flashcards):
                questions.append(flashcards[i][3:].strip())
                answers.append(flashcards[i+1][3:].strip())

        df = pd.DataFrame({"Question": questions, "Answer": answers})
        st.success("Flashcards generated!")
        st.dataframe(df)

        st.download_button("Download CSV", df.to_csv(index=False), "flashcards.csv", "text/csv")
        st.download_button("Download JSON", df.to_json(orient="records"), "flashcards.json", "application/json")
