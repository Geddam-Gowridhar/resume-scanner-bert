from pdfminer.high_level import extract_text

def extract_resume_text(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        raise RuntimeError(f"Error extracting text from PDF: {e}")