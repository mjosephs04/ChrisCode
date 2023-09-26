import datetime
import requests
import numpy as np
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Define the URL for accessing the Shopify store's API
url = 'https://7e9f940f3dbb4372bc2c756d2617ab8d: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@lovcompression.myshopify.com/admin/api/2022-04/'

# Initialize an empty list to store order information
allOrders = []
prodIDs = []
IDValues = {}
IDproducts = []
IDNumbers = []
orderNumbers= []

# Function to retrieve orders from the Shopify API
def get_orders():
    endpoint = 'orders.json'
    r = requests.get(url + endpoint)
    return r.json()

# Define a class to represent an order and its attributes
class MyOrder:
    def __init__(self, idNumber, orderNumber, Text, Font, Color, Number, Size, numFont):
        self.ID_Number = idNumber
        self.orderNumber = orderNumber
        self.Text = Text
        self.Font = Font
        self.Color = Color
        self.Number = Number
        self.Size = Size
        self.numFont = numFont

# Function to search for orders, extract customization information, and create MyOrder instances

def orderSearch():
    orders = get_orders()
    namer = 0.1

    if 'orders' in orders:

        for order in orders['orders']:
            # Create a new MyOrder instance with empty attributes
            myOrder = MyOrder(order["id"], order["order_number"], "", "", "", "", "", "")
            IDNumbers.append(order["id"])
            orderNumbers.append(order["order_number"])

            # Extract customization information from line items
            lineItems = order["line_items"][0]["properties"]
            productID = float(order["line_items"][0]["product_id"])
            # print(type(productID))

            if productID not in prodIDs:
                prodIDs.append(productID)
                IDValues[productID] = {}
                IDproducts.append(productID)
            
            else: 
                # print(type(productID))
                prodIDs.append(productID)
                new = productID + namer
                IDproducts.append(new)
                IDValues[productID + namer] = {}
                namer += 0.1

            for i in range(0, len(prodIDs)):
                prodIDs[i] = float(prodIDs[i])
            
            # print("len prodID: ", len(prodIDs))
            # print("len IDValue: ",len(IDValues))
            # print("len lineItems: ", len(lineItems))
            # print(lineItems)
            for i in range(0, len(lineItems)):
                # print(index)
                test = lineItems[i]["name"] # e.g. "size", "font color"
                value = lineItems[i]["value"] # e.g. "large", "blue"
                IDValues[productID][test] = value
        # print(IDValues)


def printer():
    print("Product ID")
    print("------------")
    for i in range(len(prodIDs) - 1, -1, -1):
        # print("ID Number: ",prodIDs[i])
        print("ID Number: ", IDNumbers[i])
        print("Order Number: ", orderNumbers[i])
        print(IDproducts[i], ": ", IDValues[[i]], "\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        
orderSearch()
print(prodIDs)
print(len(prodIDs))
print(len(IDValues))
print(len(orderNumbers))
print(len(IDNumbers))
# print(IDValues)
# printer()