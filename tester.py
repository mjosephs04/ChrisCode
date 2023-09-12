import datetime
import requests
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


"""
 - I gotta start by converting the API through the json converter
 - Then I gotta read the data into an array of classes
"""

url = 'https://7e9f940f3dbb4372bc2c756d2617ab8d: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@lovcompression.myshopify.com/admin/api/2022-04/'

#   https://7e9f940f3dbb4372bc2c756d2617ab8d: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@lovcompression.myshopify.com/admin/api/2022-04/orders.json

# class orderInfo:
#     def __init__(self, idNumber, orderNumber, name, ):
#         self.idNumber = idNumber
#         self.orderNumber = orderNumber
#         self.name =  name

class myOrder:
    orderID = 0
    orderNumber = 0
    Text = ""
    Font = ""
    Color = ""
    Number = ""
    Size = ""

allOrders = []

def get_orders():
    endpoint = 'orders.json'
    r = requests.get(url + endpoint)
    return r.json()

def get_specificItem(number):
    get_specificItem.number = number
    get_specificItem.number = int(get_specificItem.number)

def printer():
    i = 0
    for i in range(len(allOrders))
    print("ID Number: ", allOrders[i].idNumber)
    print("Order Number: ", allOrders[i].orderNumber)
    print("Text: ", allOrders[i].Text)
    print("Font: ", allOrders[i].Font)
    print("Color: ", allOrders[i].Color)
    print("Number: ", allOrders[i].Number)
    print("Size: ", allOrders[i].Size)

def lineItemSearch():
    # inside the line_items portion
    global specificOrder

    lineItems = specificOrder["line_items"][0]["properties"]
    index = 0
    while index < len(lineItems) - 1:
        index = index + 1 
        test = lineItems[index]["name"]
        value = lineItems[index]["value"]
        if test == "text":
            myOrder.Text =  value
        elif test == "Choose Font":
            myOrder.Font = value
        elif test == "Choose a Color":
            myOrder.Color = value
        elif test == "Size":
            myOrder.Size = value
        elif test == "Custom Number":
            myOrder.Number = value

def orderSearch():

    i = 0
    orders = get_orders()
    if 'orders' in orders:
        specificOrder = orders['orders'][i]  # Access the first order

        myOrder.idNumber = specificOrder["id"]
        myOrder.orderNumber = specificOrder["order_number"]

    # inside the line_items portion

    lineItems = specificOrder["line_items"][0]["properties"]
    index = 0
    while index < len(lineItems) - 1:
        index = index + 1 
        test = lineItems[index]["name"]
        value = lineItems[index]["value"]
        if test == "text":
            myOrder.Text =  value
        elif test == "Choose Font":
            myOrder.Font = value
        elif test == "Choose a Color":
            myOrder.Color = value
        elif test == "Size":
            myOrder.Size = value
        elif test == "Custom Number":
            myOrder.Number = value

    
allOrders.append(myOrder)

printer()
