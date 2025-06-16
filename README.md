
# 📚 Flash Card Generator using LLMs

This Streamlit web app allows users to generate study flashcards (Question-Answer pairs) automatically from uploaded text or PDF content using OpenAI’s GPT-3.5 language model.

🔗 Try the app live: [https://flash-card-generator.streamlit.app](https://flash-card-generator.streamlit.app)

---

## ✨ Features

- Upload .txt or .pdf files  
- Or paste raw text manually  
- Generates 10–15 Q&A flashcards using GPT-3.5  
- Download flashcards in CSV or JSON format  
- Responsive and clean Streamlit UI  

---

## 📸 Demo

Upload your notes or PDF → Click “Generate Flashcards” → Done!  
You can now download or study from generated cards right away.

---

## 🚀 Run Locally

Follow these steps if you want to run this app on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/madhavgumber/Flash-Card-Generator.git
cd Flash-Card-Generator
````

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up OpenAI API Key

Create a file named secrets.toml inside the .streamlit folder:

📁 .streamlit/secrets.toml

```toml
OPENAI_API_KEY = "your_openai_api_key_here"
```

Never commit your actual API key to GitHub! The secrets.toml file is already ignored via .gitignore.

### 5. Run the App

```bash
streamlit run app.py
```

The app should open automatically in your browser at [http://localhost:8501](http://localhost:8501)

---

## 🧠 Powered By

* [OpenAI GPT-3.5 Turbo](https://platform.openai.com/)
* [Streamlit](https://streamlit.io/)
* [PyPDF2](https://pypi.org/project/PyPDF2/)
* [Pandas](https://pandas.pydata.org/)

---

## 🙋‍♂️ Want to Contribute?

Pull requests are welcome! Feel free to fork the repo and submit improvements or additional features.

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Made with ❤️ by [Madhav Gumber](https://github.com/madhavgumber)(https://www.linkedin.com/in/madhav-gumber/)


Let me know if you'd like:

- A logo or badge section  
- GIFs/screenshots embedded  
- Deployment instructions (Streamlit Cloud, Hugging Face, etc.)

Happy shipping 🚀

