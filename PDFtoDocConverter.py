# pip install PDF2Docx
from pdf2docx import parse
import os

# Lista os arquivos pdf na pasta e converte pra Word (Docx)
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        pdf_file = file
        word_file = f"{pdf_file}.docx"
        parse(pdf_file, word_file, start=0, end=None)