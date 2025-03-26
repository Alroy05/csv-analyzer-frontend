# 📊 RAG CSV Analyzer

RAG CSV Analyzer is a web-based tool that allows users to upload, analyze, and query CSV files using a powerful backend API. The application provides an intuitive interface for previewing data, querying datasets, and managing uploaded files with ease.

## 🖼️ Project Screenshots

![Screenshot 1](/assets/ss1.png)
![Screenshot 2](/assets/ss2.png)

## 🔗 Deployed URL
```bash
   https://csv-analyzer-alroy.streamlit.app/
   ```
   
## 🚀 Installation Steps

### Frontend Setup (Streamlit App)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/csv-analyzer-frontend.git
   cd csv-analyzer-frontend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**
   - Inside the project folder, create a `.env` file and add the backend API URL:
   ```env
   API_URL=http://127.0.0.1:8000
   ```

5. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```

## 🔗 Backend Repository
The backend for this project is available at:
[CSV Analyzer Backend](https://github.com/Alroy05/csv-analyzer-backend)

---

Made with ❤️ by Alroy

