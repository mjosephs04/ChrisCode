from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def makePDF(color):
    c = canvas.Canvas("pdfs/" + color + ".pdf", pagesize=letter)
    for i in range(len(hash.listOfColorLists[color])):
            c.drawString(30, 750 - (10 * i), hash.listOfColorLists[color][i].text)
            c.drawString(150, 750 - (10 * i), hash.listOfColorLists[color][i].font)
    c.save()