import PyPDF2

pdf = open('./python_tutorial.pdf', 'rb')
watermark = open('./watermark.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf)
pdf_writer = PyPDF2.PdfWriter()
page_obj = pdf_reader.pages[0]
page_obj.merge_page(PyPDF2.PdfReader(watermark).pages[0])
pdf_writer.add_page(page_obj)

with open('water_marked.pdf', 'wb') as f:
    pdf_writer.write(f)

