import fitz  # PyMuPDF

def read_pdf(pdf_file):
    # Open the PDF file
    try: 
        doc = fitz.open(stream= pdf_file.read(), filetype = "pdf")
        text = ""
    except Exception as e:
        print(f"ERROR while reading opening pdf with fitz: {e}")
        return None
    
    # Iterate through each page of the PDF
    for page in doc:
        # Extract text from the current page
        text += page.get_text()
    
    # Close the document
    doc.close()
    return text


