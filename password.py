import PyPDF2

pdf = open('./water_marked.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf)
pdf_writer = PyPDF2.PdfWriter()

for page in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page])

pdf_writer.encrypt('123')

with open('encrypted.pdf', 'wb') as f:
    pdf_writer.write(f)
