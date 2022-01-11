from typing import TypedDict
from PyPDF2 import PdfFileWriter, PdfFileReader

f = open("recap.pdf", "rb")

reader = PdfFileReader(f)

page_0 = reader.getPage(0)
text = page_0.extractText()

text = text.replace("Ò",'"').replace('‘', "è")

f.close()

print(text)