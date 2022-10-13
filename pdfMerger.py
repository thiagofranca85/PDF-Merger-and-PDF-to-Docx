from email.policy import strict
# Instalar o PyPDF2 usando pip install PyPDF2
import PyPDF2
import os

# Abrevia em merger o PdfFileMerger
merger = PyPDF2.PdfFileMerger(strict=False)

# Lista todos os arquivos da pasta, o IF separa apenas os PDFs e faz a união.
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

# Gera o arquivo com os PDFs Combinados
merger.write('PDFs Combinados.pdf')
merger.close()