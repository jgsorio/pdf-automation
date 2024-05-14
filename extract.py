import PyPDF2

pdf = open('./python_tutorial.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf)
page_obj = pdf_reader.pages[1]
print(page_obj.extract_text())
