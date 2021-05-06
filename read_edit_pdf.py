import PyPDF2
import os

os.chdir('C:\\Users\Saimun\Python ardit\Reading and editing pdfs')

pdfFile = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)

page= reader.getPage(0)

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

