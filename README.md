# 🚀 PDFWS — Lightning-Fast PDF Merger

> Merge multiple PDFs effortlessly — right from your browser, in the exact order you upload them.

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

## 🎮 DEMO

Will be added later

## ✨ Features

* 📂 Upload multiple PDF files
* 🔀 Merge in **exact upload order**
* ⚡ Fast and lightweight processing
* 📥 One-click download of merged file
* 🧹 Automatic cleanup after download
* 🎯 Simple and intuitive UI powered by Streamlit

---

## 🖼️ Preview

> Clean, minimal interface focused on productivity

```
Upload → Arrange → Merge → Download
```

---

## 🛠️ Tech Stack

* 🐍 Python
* ⚡ Streamlit
* 📚 PyPDF2

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/SedeWahlid/simple_PDF_Merger.git
cd simple_PDF_Merger
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

Then open your browser and:

1. Upload 2 or more PDF files
2. Click **Submit**
3. Download your merged PDF 🎉

---

## 🧠 How It Works

* Files are uploaded via Streamlit UI
* `PdfMerger` from PyPDF2 combines them sequentially
* A temporary file (`mergedPDF.pdf`) is generated
* File is offered for Preview and download
* File is deleted automatically after serving

---

## 📁 Project Structure

```
📦 pdfws
 ┣ 📜 main.py
 ┣ 📜 .gitignore
 ┣ 📜 README.md
 ┣ 📜 LICENSE
 ┗ 📜 requirements.txt
```

---

## ⚠️ Notes

* Requires **at least 2 PDFs** to merge
* Max upload size: **500MB per file**

---

## 📄 License

This project is licensed under the APACHE 2.0 License.

---