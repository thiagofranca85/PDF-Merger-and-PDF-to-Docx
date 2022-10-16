# pip install PDF2Docx
# Se estiver usando a ultima versão do Python, talvez não funcione corretamente o pdf2docx, basta rodar o python em uma das versões anteriores 3.9, 3.8 .. por exemplo.
from pdf2docx import parse
import os

# Lista os arquivos pdf na pasta e converte pra Word (Docx)
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        docxfile = file.replace(".pdf",".docx")
        parse(file, docxfile, start=0, end=None)