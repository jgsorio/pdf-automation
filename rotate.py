import PyPDF2

def PDFRotate(pdf, angle, filename):
    pdf = open(pdf, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf)
    pdf_writer = PyPDF2.PdfWriter()
    for page in range(len(pdf_reader.pages)):
        page_obg = pdf_reader.pages[page]
        page_obg.rotate(angle)
        pdf_writer.add_page(page_obg)

    with open(filename, 'wb') as f:
        pdf_writer.write(f)

PDFRotate('python_tutorial.pdf', 90, 'rotated.pdf')