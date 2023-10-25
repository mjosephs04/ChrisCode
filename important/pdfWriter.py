from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import customHashish as hash

startHeight = 750
pageWidth = 400
currentWidth = 30

"""
Needs to read a font and return a number
"""

"""
Takes the length of the font and updates the size
"""

# registering fonts
pdfmetrics.registerFont(TTFont('Marker', 'Bangers.ttf'))
pdfmetrics.registerFont(TTFont('Tough', 'BlackOpsOne-Regular.ttf'))
pdfmetrics.registerFont(TTFont('College', 'colleges.ttf'))
pdfmetrics.registerFont(TTFont('Iceberg', 'Iceberg.ttf'))
pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Jersey', 'sportsjersey.ttf'))
pdfmetrics.registerFont(TTFont('Asos', 'full_Pack_2025.ttf'))
pdfmetrics.registerFont(TTFont('Adventure', 'SF Fedora.ttf'))
pdfmetrics.registerFont(TTFont('Sporty', 'Calibri Bold.TTF'))
pdfmetrics.registerFont(TTFont('Burny', 'Burny.ttf'))
pdfmetrics.registerFont(TTFont('Rounded', "Dosis-Medium.ttf"))

avgFont = 75
fonts = {}
fonts["Marker"] = avgFont
fonts["Tough"] = avgFont - 5
fonts["College"] = avgFont
fonts["Iceberg"] = avgFont
fonts["Roboto"] = avgFont
fonts["Jersey"] = avgFont
fonts["Asos"] = avgFont - 5
fonts["Adventure"] = avgFont
fonts["Sporty"] = avgFont
fonts["Burny"] = avgFont
fonts["Rounded"] = avgFont

def fontSize(font):
    return fonts[font]

def makePDF(color):
    global currentWidth
    pageHeight= 720
    c = canvas.Canvas("pdfs/" + color + ".pdf", pagesize=letter)
    if (len(hash.listOfColorLists[color]) != 0):
            for i in range(len(hash.listOfColorLists[color])):
                custom =  hash.listOfColorLists[color][i]
                c.setFont(custom.font, fontSize(custom.font))
                stringWidth = pdfmetrics.stringWidth(custom.text, custom.font, fontSize(custom.font))

               
                if(custom.text == "Wolf Pack" or custom.text == "Respect"):
                    print("The font is: ", custom.font)
                if currentWidth + stringWidth > pageWidth:
                    currentWidth = 30
                    pageHeight -= 144
                
                    if pageHeight <= 0:
                        c.showPage()
                        pageHeight = 730
                        c.setFont(custom.font, fontSize(custom.font))
                
                
                c.drawString(currentWidth, pageHeight, custom.text)
                currentWidth += stringWidth + 20

                # ascent = pdfmetrics.getAscent(custom.font, fontSize(custom.font))
                # descent = pdfmetrics.getDescent(custom.font, fontSize(custom.font))
                # stringHeight = ascent - descent

            
            c.save()

def makePDFs():
    global currentWidth
    for color in hash.listOfColorLists:
        pageHeight = 750

        if (len(hash.listOfColorLists[color]) != 0):
            
            c = canvas.Canvas("pdfs/" + color + ".pdf", pagesize=letter)
            for i in range(len(hash.listOfColorLists[color])):
                custom =  hash.listOfColorLists[color][i]
                c.setFont(custom.font, fontSize(custom.font))
                c.drawString(currentWidth, pageHeight, custom.text)
                stringWidth = pdfmetrics.stringWidth(custom.text, custom.font, fontSize(custom.font))
                currentWidth += stringWidth

                if currentWidth > pageWidth:
                    currentWidth = 30
                    pageHeight -= 144
            c.save()