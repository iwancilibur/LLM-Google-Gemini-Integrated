# Konsultasi cinta dengan integrasi Ai LLM Google Gemini:
Ilustrasi ini menggambarkan sebuah sesi "Konsultasi Cinta" yang canggih dan modern dengan integrasi AI LLM (Large Language Model) Google Gemini. Di dalam gambar, terlihat elemen-elemen romantis yang berpadu dengan teknologi—simbol hati, percakapan digital, serta perangkat AI yang membantu memberikan nasihat cinta secara personal. Ini mencerminkan era baru di mana perasaan dan teknologi berpadu, memungkinkan siapa pun untuk curhat, mendapatkan nasihat puitis, lucu, atau formal tentang cinta dengan bantuan kecerdasan buatan.
!Demo](static/konsultasi.png)

# Fiture
✅PDF lokal (jika tersedia)
✅Sumber online (misal artikel tentang cinta dan hubungan)
✅Pengetahuan dasar tentang cinta (gaya puitis/lucu/formal)
✅Output dari model Gemini (menggunakan konteks di atas)

# Program ini sudah dioptimalkan untuk:
✅Ketepatan diagnosa (dengan cross-checking sumber online)
✅Kenyamanan pengguna (antarmuka intuitif) "Masih perlu rapihin lagi"

# Teknologi:
✅ Gemini Genai
✅ Langchain
✅ Flask
✅ Mysql

# Buat environment baru
- python -m venv venv
- source venv/bin/activate  # Untuk Linux/Mac
- venv\Scripts\activate  # untuk Windows

# Struktur Folder yang Direkomendasikan
love_consultation_app/
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
├── data/
│   └── love_articles.pdf
├── requirements.txt

# Install dependencies
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install -qU langchain_community
pip install --upgrade langchain-community

# Daftar Gemini Ai
Dapatkan API Key Gemini [GRATIS]
1. Kunjungi Google AI Studio. https://aistudio.google.com/
2. Buat API Key baru.
3. Simpan key di variabel "GOOGLE_API_KEY" dalam program app.py

# Ngrok
- Install Windows : https://dashboard.ngrok.com/get-started/setup/windows
- ngrok config add-authtoken aut_kamu
- ngrok http http://127.0.0.1:5000

# Untuk CPU (pilihan paling umum)
- pip install faiss-cpu

# Untuk GPU NVIDIA (jika Anda memiliki GPU CUDA)
- pip install faiss-gpu

# Donate
- Author : Iwan Cilibur
- Traktir saya : https://dunyotech.myr.id/payme