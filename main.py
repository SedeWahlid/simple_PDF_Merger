import streamlit as st 
from PyPDF2 import PdfMerger
from time import sleep
from os import remove,path


FILE_PATH = "mergedPDF.pdf"

#################################################
# BACKEND
#################################################

# merges the uploaded pdf files by there upload order
def merge_files(files: list[list]):
    try:
        merger = PdfMerger()
        for file in files:
            merger.append(file)
        merger.write("mergedPDF.pdf")
        merger.close()
    except Exception as e:
        st.error(f"Error while merging with error: {e}")

# downloading file and cleaning up afterwards
def download_file():
    try:
        with open("mergedPDF.pdf","rb") as file:
            preview_pdf(file)
            st.download_button("Download",file,"mergedPDF.pdf","application/pdf")
            
        if path.exists(FILE_PATH):
            remove(FILE_PATH)
    except Exception as e:
        st.error(f"Could not create downloadable with error: {e}")

def preview_pdf(file):
    st.subheader("Merged PDF preview:")
    try:
        st.pdf(file)
    except Exception as e:
        st.error(f"Preview couldn't load with error: {e}")
    

#################################################
# STREAMLIT 
#################################################

st.set_page_config(layout="wide", page_title="PDFWS")
st.title("PDFWS")
st.caption("Merges PDF's by there upload order. So be careful when uploading :) Further notice, you must upload at least 2 files and for now the upload size is bounded at 500MB.") 
files = st.file_uploader("Upload PDF",accept_multiple_files=True,type="pdf", max_upload_size=500) # only pdf files and multiple files and 500MB upload size

# creating the download button and its process whenever we press the submit button
if len(files) > 1:
    button_pressed = st.button("Submit", on_click=merge_files, args=(files,))
    if button_pressed:
        sleep(2)
        download_file()
