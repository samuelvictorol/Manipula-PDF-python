import os
from PyPDF2 import PdfReader, PdfWriter

diretorio = "./filesToBeSeparated"
diretorio_separado = "./separatedFiles"

if not os.path.exists(diretorio_separado):
    os.makedirs(diretorio_separado)

for filename in os.listdir(diretorio):
    if filename.endswith(".pdf"):
        pdf_file_path = os.path.join(diretorio, filename)
        with open(pdf_file_path, "rb") as input_file:
            pdf_reader = PdfReader(input_file)
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):
                pdf_writer = PdfWriter()
                output_pdf_path = os.path.join(diretorio_separado, f"{os.path.splitext(filename)[0]}_page{page_num + 1}.pdf")
                pdf_writer.add_page(pdf_reader.pages[page_num])
                with open(output_pdf_path, "wb") as output_file:
                    pdf_writer.write(output_file)

print("Páginas separadas geradas com sucesso!")
