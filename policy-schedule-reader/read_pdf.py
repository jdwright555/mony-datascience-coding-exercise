def load_cvdata_from_pdf(file_path):
    with open(file_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    return pdf_bytes