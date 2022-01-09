import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
import win32com.client
import os
import shutil
from cryptography.fernet import Fernet
pdfFileObj = open("1697.pdf", "rb")
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
print("Please enter the password of the pdf file> ")
encryptattempt = input()
if password == encryptattempt:
    with open("crash_report_encrypted.pdf", "wb") as f:
        out.write(f)  # Write pages to crash_report_encrypted.pdf
else:
    print("Alexa Intruder Alert")
    print("Just kidding")

#Lines below converts PDF to Word
word = win32com.client.Dispatch("Word.Application")
word.visible = 1 #Set this to 0 if you dont want to see the word application but it is cool when you see the process kek.
wordObj = word.Documents.Open(os.path.abspath("AAR69-06.pdf")) # Crash report pdf
wordObj.SaveAs("1697.docx", FileFormat=16) #FF=16 means .docx
#Lines below encrypts the file with random generated Fernet key.
key = Fernet.generate_key()
with open("filekey.key", "wb") as filekey:
    filekey.write(key)
    # Save the key and read it
with open("filekey.key", "rb") as filekey:
    key = filekey.read()
fernet = Fernet(key)
os.chdir(r"C:\Users\emosc\OneDrive\Belgeler") #Annoying code at line 32 saves the document to only Documents folder.
shutil.copy("1697.docx", r"C:\Users\emosc\PycharmProjects\pythonProject6") #Copy that document and yeet it to project folder.
os.chdir(r"C:\Users\emosc\PycharmProjects\pythonProject6") #Come back to project folder.
with open("1697.docx","rb") as file:
    original = file.read()
encrypteddocx = fernet.encrypt(original) #Encrypt the file
with open("1697_encrypted.docx","wb") as encrypted_file:
    encrypted_file.write(encrypteddocx)

# Summarize the 48 lines, get a random flight crash report (1697.pdf)
# Airbus A318-111 aircraft, registration F-GUGK operated by Air France under callsign AFR 989Z
# Encrypt the pdf file to crash_report_encrypted.pdf
# Generate a Fernet key
# Encrypt the word file and write the encryption to 1697_encrypted.docx.
# AAR69-06.pdf also works but it is a very old document and it is very messy.

#Lines below decrypts the document.
decrypted = fernet.decrypt(encrypteddocx)
with open("1697_decrypted.docx","wb") as decrypted_file:
    decrypted_file.write(decrypted)

#Project grows, I encrypted two random things so far!
#TODO Next thing I will encrypt is a random hat JPG that my brother sells.