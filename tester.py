from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a PDF canvas
c = canvas.Canvas("test.pdf", pagesize=letter)

# Go down 3 inches
y_coordinate = 216  # 3 inches in points
c.drawString(100, y_coordinate, "Text at 3 inches down")

# Close the PDF canvas
c.save()