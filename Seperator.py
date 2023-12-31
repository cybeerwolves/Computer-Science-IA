import os
import PyPDF2
from pdf2image import convert_from_bytes
import io

def getImage(page):
    image = page.get_contents()
    output_stream = io.BytesIO()
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(page)
    pdf_writer.write(output_stream)
    byte_data = output_stream.getvalue()
    ret = convert_from_bytes(byte_data)[0]
    return ret

def run():
    PDFcounter = 0
    existing = 0
    # Set the input and output paths
    path = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/Slides/'
    files = os.listdir(path)
    page_num = 0
    for file in files:
        if file.endswith(".pdf"):
            input_path = os.path.join(path, f'{files[PDFcounter]}')

            location = input_path.split('/')
            output_path = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlidesImage/'

            # Create the output folder if it doesn't exist
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            # Open the PDF file
            with open(input_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                # Loop through each page of the PDF
                page_num = 0
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pil_image = getImage(page)

            # Save the image as a JPEG file
                    output_filename = os.path.join(output_path, f'page{existing+page_num+1}.jpg')
                    pil_image.save(output_filename, 'JPEG')
        existing = existing + page_num
        PDFcounter = PDFcounter + 1
run()            


                    