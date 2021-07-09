from docx import Document
import csv

doc = Document('test.docx')
words = {}
for para in doc.paragraphs:
    line = para.text
    for word in line.split(' '):
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
print(words)

