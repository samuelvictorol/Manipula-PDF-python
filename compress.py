import os
from PyPDF2 import PdfMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

diretorio = "./filesToBeCompressed"
diretorio_comprimido = "./compressedFiles"

pdf_files = []

for filename in os.listdir(diretorio):
    if filename.endswith(".pdf"):
        pdf_files.append(os.path.join(diretorio, filename))

pdf_files.sort(key=lambda x: int(os.path.basename(x).split('.')[0]))

pdf_merger = PdfMerger()

for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

pdf_comprimido = os.path.join(diretorio_comprimido, "pdf_comprimido.pdf")

if not os.path.exists(diretorio_comprimido):
    os.makedirs(diretorio_comprimido)

with open(pdf_comprimido, "wb") as output_file:
    pdf_merger.write(output_file)

c = canvas.Canvas(os.path.join(diretorio_comprimido, "pdf_comprimido_compress.pdf"), pagesize=letter)
c.drawString(100, 100, "PDF Comprimido")
c.save()

print("PDF comprimido gerado com sucesso!")
