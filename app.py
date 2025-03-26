import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")  # Default to local if not set

st.title("📊 RAG CSV Analyser")

# 📌 Upload CSV File
st.subheader("Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# ✅ **Preview before uploading**
if uploaded_file:
    st.write("🔍 **Preview before Uploading:**")
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))  # Show first 5 rows

if st.button("Upload"):
    if uploaded_file:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        response = requests.post(f"{API_URL}/upload", files=files)
        if response.status_code == 200:
            st.success(f"File uploaded successfully! File ID: {response.json()['file_id']}")
        else:
            st.error("Upload failed!")

# 📌 List Available Files (MongoDB)
st.subheader("Available Files")
response = requests.get(f"{API_URL}/files")
if response.status_code == 200:
    files = response.json()["files"]
    if files:
        file_id = st.selectbox("Select a file:", [f"{f['file_name']} ({f['file_id']})" for f in files])
        selected_file_id = file_id.split("(")[-1][:-1]  # Extract file_id

        # ✅ **Preview after uploading**
        if st.button("Preview CSV"):
            response = requests.get(f"{API_URL}/preview/{selected_file_id}")
            if response.status_code == 200:
                df = pd.DataFrame(response.json())  # Convert JSON to DataFrame
                st.write(df)
            else:
                st.error("Failed to fetch CSV preview.")

        # 📌 Query CSV
        st.subheader("Query CSV")
        query_text = st.text_input("Enter your query:")
        if st.button("Ask Query"):
            response = requests.post(f"{API_URL}/query", json={"file_id": selected_file_id, "query": query_text})
            if response.status_code == 200:
                st.write(response.json()["response"])
            else:
                st.error("Failed to retrieve response.")

        # 📌 Delete File
        if st.button("Delete File"):
            response = requests.delete(f"{API_URL}/file/{selected_file_id}")
            if response.status_code == 200:
                st.success("File deleted successfully!")
            else:
                st.error("Failed to delete file.")
    else:
        st.write("No files available.")
