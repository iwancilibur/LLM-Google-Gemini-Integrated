import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import google.generativeai as genai

app = Flask(__name__)

# Konfigurasi Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) #isi Api nya disini

model = genai.GenerativeModel("gemini-2.0-flash")

# Integrasi pengetahuan
def get_love_knowledge(user_question):
    knowledge = ""

    # 1. Dari PDF lokal
    pdf_path = "data/love_articles.pdf"
    if os.path.exists(pdf_path):
        try:
            loader = PyPDFLoader(pdf_path)
            pages = loader.load_and_split()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            docs = text_splitter.split_documents(pages)
            knowledge += "\n".join([doc.page_content for doc in docs[:2]]) + "\n\n"
        except Exception as e:
            print(f"[PDF] Error: {str(e)}")

    # 2. Dari situs online
    try:
        urls = [
            "https://www.psychologytoday.com/us/topics/relationships",
            "https://id.wikipedia.org/wiki/Cinta"
        ]
        for url in urls:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                paragraphs = [p.get_text() for p in soup.find_all('p')]
                knowledge += f"[Sumber: {url}]\n" + "\n".join(paragraphs[:3]) + "\n\n"
    except Exception as e:
        print(f"[Online] Error: {str(e)}")

    # 3. Pengetahuan dasar cinta
    base_knowledge = """
    Cinta adalah perasaan mendalam yang tak selalu mudah dijelaskan.
    Ada cinta romantis, cinta platonis, dan cinta penuh pengorbanan.
    Dalam hubungan, komunikasi, kepercayaan, dan empati adalah fondasi penting.
    
    Gaya puitis: "Cinta itu seperti angin—tak terlihat, tapi terasa sampai ke tulang."
    Gaya lucu: "Cinta itu seperti WiFi, sinyalnya kuat di awal, tapi lama-lama lelet juga."
    Gaya formal: "Hubungan cinta yang sehat melibatkan keterbukaan, rasa saling menghargai, dan kemampuan menyelesaikan konflik secara dewasa."
    """

    knowledge += base_knowledge
    return knowledge

# Rute halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Rute hasil konsultasi
@app.route('/result', methods=['POST'])
def result():
    user_input = request.form['user_input']
    style = request.form.get('style', 'puitis')

    knowledge = get_love_knowledge(user_input)

    prompt = f"""
    Kamu adalah pakar cinta bergaya {style}. 
    Berikut pertanyaan pengguna: "{user_input}"
    
    Gunakan pengetahuan di bawah ini untuk memberi saran yang mendalam, sesuai gaya:
    {knowledge}
    
    Berikan jawaban dengan sentuhan {style} (puitis/lucu/formal), dan beri penutup yang menggugah hati.
    """

    try:
        response = model.generate_content(prompt)
        hasil = response.text
    except Exception as e:
        hasil = f"Terjadi kesalahan saat memproses permintaan: {str(e)}"

    return render_template('result.html', question=user_input, answer=hasil)

if __name__ == '__main__':
    app.run(debug=True)
