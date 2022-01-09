import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
pdfFileObj = open("AAR69-06.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj  = pdfReader.getPage(0) #Get page number
print(pageObj.extractText()) #Extract text and print the page number above
number = pdfReader.numPages #Get number of pages
out = PdfFileWriter() #Create a pdf file for writing
for index in range(number):
    page = pdfReader.getPage(index)
    out.addPage(page)
    #Adding all pages in number range to new pdf file
password = "tekeglencem31"
out.encrypt(password)
with open("crash_report_encrypted.pdf","wb") as f:
    out.write(f) #Write pages to crash_report_encrypted.pdf
