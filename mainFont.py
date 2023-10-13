import requests
import customHashish as hash


# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont

# Define the URL for accessing the Shopify store's API
url = 'https://a49ba18159fe5c18878c02cd077c773b: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@lovcompression.myshopify.com/admin/api/2022-04/'


# Function to retrieve orders from the Shopify API


def get_orders():
    endpoint = 'orders.json'
    r = requests.get(url + endpoint)
    return r.json()


class Order:
    orderID = ""
    lineItems = []
    lineItemCount = 0

    def Order(self):
        self.orderID = ""
        self.lineItems = []
        self.lineItemCount = 0

    def setOrderID(self, specificOrderID):
        self.orderID = specificOrderID

    def addLineItem(self, liney):
        self.lineItems.append(liney)
        self.lineItemCount += 1

    def printOrder(self):
        # print(self.orderID)
        print(len(self.lineItems))  # print the line Item at index i
        for item in self.lineItems:
            print(item)


"""|
getSpecificProductID

gets the product ID from a line item

parameters:
    item: the line item - order["line_items"][0]["properties"]

output:
    returns the productID as a string
"""


def getSpecificProductID(item):
    return int(item["product_id"])


# initialize lists
listOfOrders = []  # list of classess
listOfItems = []  # all the line items that have

"""
data search: iterates through the orders and makes a list of class Orders
returns that list
"""


def dataSearch():
    orderData = get_orders()
    i = 0
    for order in orderData["orders"]:
        # creating new instance of order class
        myOrder = Order()
        myOrder.Order()
        myOrder.setOrderID(order["order_number"])

        """
        gathering product ID and customization info
        """
        lineItems = order["line_items"][0]["properties"]
        # converting to float so I can manipulate it if needed

        for i in range(0, len(order["line_items"])):
            myOrder.addLineItem(order["line_items"][i])
            listOfItems.append(order["line_items"][i])

        listOfOrders.append(myOrder)


dataSearch()


def printer():
    for i in len(listOfOrders):
        listOfOrders[i].printOrder()


"""
gets each item's product ID
"""
for item in listOfItems:
    productID = getSpecificProductID(item)

    hash.getDataFromLineItem(productID, item)

    hash.listOfColorLists["White"]

# for color in hash.colors:
#     print(color)
#     print("Length!: ",len(hash.listOfColorLists[color]))
#     if(len(hash.listOfColorLists[color]) != 0):
#         for i in range(len(hash.listOfColorLists[color])):
#             hash.listOfColorLists[color][i].print()

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Create a new PDF document
c = canvas.Canvas("test.pdf", pagesize=letter)

#registering fonts
pdfmetrics.registerFont(TTFont('Marker', 'Bangers.ttf'))
pdfmetrics.registerFont(TTFont('Tough', 'BlackOpsOne-Regular.ttf'))
pdfmetrics.registerFont(TTFont('College', 'college.ttf'))
pdfmetrics.registerFont(TTFont('Iceberg', 'Iceberg.ttf'))
pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Jersey', 'sportsjersey.ttf'))
pdfmetrics.registerFont(TTFont('Asos', 'full_Pack_2025.ttf'))
pdfmetrics.registerFont(TTFont('Adventure', 'SF Fedora.ttf'))
pdfmetrics.registerFont(TTFont('Sporty', 'Calibri Bold.TTF'))
pdfmetrics.registerFont(TTFont('Burny', 'Burny.ttf'))


# Set the title and author metadata for the PDF (optional)
# c.setTitle("My Basic PDF")
# c.setAuthor("I am a huble slave")

def makePDF(color):
    c = canvas.Canvas(color + ".pdf", pagesize=letter)
    # for color in hash.colors:
    # print(hash.listOfColorLists["Black"])
    if (len(hash.listOfColorLists[color]) != 0):
        for i in range(len(hash.listOfColorLists[color])):
            c.setFont(hash.listOfColorLists[color][i].font, 25)                         # setting the font
            c.drawString(70, 750 - (40 * i), hash.listOfColorLists[color][i].text)      # putting text onto page
            #c.drawString(110, 750 - (10 * i), hash.listOfColorLists[color][i].font)
            #c.drawString(175, 750 - (40 * i), 'Tough')
    c.save()


makePDF("White")
# print(hash.listOfColorLists["Black"][0].font)