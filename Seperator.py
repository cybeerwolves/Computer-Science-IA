import os
import PyPDF2
from pdf2image import convert_from_bytes
import io


PDFcounter = 0
# Set the input and output paths
path = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/Slides/'
files = os.listdir(path)
for file in files:
    if file.endswith(".pdf"):
        input_path = os.path.join(path, f'{files[PDFcounter]}')

        location = input_path.split('/')
        output_path = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlidesImage/'+location[len(location) - 1]

        # Create the output folder if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Open the PDF file
        with open(input_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Loop through each page of the PDF
            for page_num in range(len(pdf_reader.pages)):
                # Get the page and convert it to an image
                page = pdf_reader.pages[page_num]
                image = page.get_contents()
                output_stream = io.BytesIO()
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.add_page(page)
                pdf_writer.write(output_stream)

                byte_data = output_stream.getvalue()

        # Convert the byte data to a PIL Image object using pdf2image
                pil_image = convert_from_bytes(byte_data)[0]

        # Save the image as a JPEG file
                output_filename = os.path.join(output_path, f'page{page_num+1}.jpg')
                pil_image.save(output_filename, 'JPEG')
    PDFcounter = PDFcounter + 1
            


                