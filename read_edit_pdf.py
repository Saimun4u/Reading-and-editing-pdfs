import PyPDF2
import os

# Read pdf file

os.chdir('C:\\Users\Saimun\Python ardit\Reading and editing pdfs')

pdfFile = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)

page= reader.getPage(0)

# for pageNum in range(reader.numPages):
#     print(reader.getPage(pageNum).extractText())

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('mergedminutes.pdf', 'wb')

writer.write(outputFile)

outputFile.close()

pdf1File.close()
pdf2File.close()