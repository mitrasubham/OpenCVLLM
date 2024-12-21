#PDF to image 

from pdf2image import convert_from_path

# Store Pdf with convert_from_path function
#images = convert_from_path('COMMERCIAL WORK.pdf')

#for i in range(len(images)):
  
      # Save pages as images in the pdf
    #images[i].save('page'+ str(i) +'.jpg', 'JPEG')


#We  can use the `PyMuPDF` library to convert each page of a PDF into an image file. Here’s a simple script to achieve that:
import fitz  # PyMuPDF

def pdf_to_images(pdf_path, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document.load_page(page_number)
        
        # Render the page to a pixmap (image)
        pix = page.get_pixmap()
        
        # Define the output file path
        output_path = f"{output_folder}/page_{page_number + 1}.png"
        
        # Save the image
        pix.save(output_path)
    
    # Close the PDF document
    pdf_document.close()

# Example usage
pdf_to_images("COMMERCIAL WORK.pdf", "output_images")