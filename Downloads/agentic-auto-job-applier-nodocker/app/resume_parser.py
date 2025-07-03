import docx2txt
from pdfminer.high_level import extract_text

def parse_resume(file):
    if file.name.endswith(".pdf"):
        return extract_text(file)
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    else:
        return ""