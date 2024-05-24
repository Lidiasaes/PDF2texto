import streamlit as st 
import pdf2text
from pdf2text import read_pdf



st.set_page_config(page_title='PDF2Texto', page_icon=":tada:", layout="wide")
# HEADER
with st.container():
    st.title(":violet[_PDF2TEXTO_] :sparkles:")
    st.subheader(""":grey[Welcome to _your PDF to text converter_ for FREE]""", divider="orange")


# Upload a file 
def load_file():
    file = st.file_uploader(":grey[Select your pdf file and... let's go!]", type= ["pdf"], accept_multiple_files=False)
    if file is not None: 
        try:                     
            # Read and print the text from the PDF
            pdf_text = read_pdf(file)
            if pdf_text:
                st.write(pdf_text)
                download_txt_converted_file(pdf_text)
            else:
                st.error("Could not read text from the pdf")
        except Exception as e:
            st.error(f"An error occurred while reading the PDF: {e}")
            st.warning("OOOooops! Your file seems to be empty\n Try with another pdf")



def download_txt_converted_file(text_content):
    if text_content:
        st.download_button("Download your text content!", text_content, file_name="pdf2texto_converted.txt")
        st.write("\n\n:violet[Thank you! :confetti_ball:]")


load_file()
