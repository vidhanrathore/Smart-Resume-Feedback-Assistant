import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

# === USAGE EXAMPLES ===

# For PDF file

if __name__ == "__main__":
    with open("rimjhim_resume.pdf", "rb") as pdf_file:
        pdf_text = extract_text_from_pdf(pdf_file)
        print("Text from PDF:")
        print(pdf_text)

# # For DOCX file
# with open("example.docx", "rb") as docx_file:
#     docx_text = extract_text_from_docx(docx_file)
#     print("\nText from DOCX:")
#     print(docx_text)
