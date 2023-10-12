from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Create a new PDF document
c = canvas.Canvas("test.pdf", pagesize=letter)

# Set the title and author metadata for the PDF (optional)
# c.setTitle("My Basic PDF")
# c.setAuthor("I am a huble slave")

def makePDF(color):
    c = canvas.Canvas(color + ".pdf", pagesize=letter)
    # for color in hash.colors:
    
    
    c.drawString(100, 750, "Hell")

# Save the PDF file
    c.save()

makePDF("Black")

