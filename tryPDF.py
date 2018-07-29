import PyPDF2


# 'rb' : as PDF are in the binary mode and r for read
file = open('BPT.pdf', 'rb')
# Read PDF file in to a variable 
reader = PyPDF2.PdfFileReader(file)
# numPages : gives the number of pages
pages = reader.numPages
print('The number of pages in the PDF are' + ' ' + str(pages))
# getPage function to directly get the particular page
page = reader.getPage(2)
print(page.extractText())
# Extract the whole PDF file
for pageno in range(pages):
    print(reader.getPage(pageno).extractText())
# new PDF writer function
writer = PyPDF2.PdfFileWriter()
for pageno in range(pages):
    pag = reader.getPage(pageno)
    writer.addPage(pag)
out = open('new_PDF.pdf', 'wb')
writer.write(out)
out.close()
file.close()