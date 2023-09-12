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

class orderInfo:
    def __init__(self, idNumber, orderNumber, name, ):
        self.idNumber = idNumber
        self.orderNumber = orderNumber
        self.name =  name

allOrders = []

def get_orders():
    endpoint = 'orders.json'
    r = requests.get(url + endpoint)
    return r.json()

def get_specificItem(number):
    get_specificItem.number = number
    get_specificItem.number = int(get_specificItem.number)

i = 0

orders = get_orders()
if 'orders' in orders:
    first_order = orders['orders'][0]  # Access the first order
    order_number = first_order['order_number']
    orderInfo.idNumber = first_order['id']
    appID = orders["orders"][0]['app_id']
    # if("properties"):
    #     name = (['orders'][i]['line_items'][get_specificItem.number]['name'])
    #     number = (['orders'][i]['line_items'][get_specificItem.number]['properties'][0]['value'])
    #     font = (['orders'][i]['line_items'][get_specificItem.number]['properties'][1]['value'])
    #     txt_color = (['orders'][i]['line_items'][get_specificItem.number]['properties'][2]['value'])
    #     size = (['orders'][i]['line_items'][get_specificItem.number]['properties'][3]['value'])

    order = orderInfo(first_order['id'], first_order['order_number'], "hi")
    # print("Order Number:", order_number)
    # print("id: ", orderInfo.idNumber)
    # print("app ID: ", appID)
    print(type(orderInfo.idNumber))
else:
    print("No orders found in the response.")


