from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import requests
import tkinter as tk
from tkinter import *
import io

# defining the gui
root = tk.Tk()
root.title('Custom Sports Sleeves')
root.geometry('700x700')

url = 'https://7e9f940f3dbb4372bc2c756d2617ab8d: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@lovcompression.myshopify.com/admin/api/2022-04/'

def get_date():
    get_date.date_1 = int(entry_date.get())
    get_date.orders = get_orders()

def get_orders():
    endpoint = f'orders.json?limit=250;created_at_max=2022-08-{get_date.date_1}T23:59:59;status=any'
    r = requests.get(url + endpoint)
    return r.json()

# Importing Fonts
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

def namePDF(pdfName):
    namePDF.pdf = canvas.Canvas(pdfName + '.pdf')
    namePDF.numberEntries = 0
    namePDF.pdf.setPageSize((648,1286))

def headbandFontSize (txt, font1):
    txtLength = len(txt)
    print(txtLength)
    if font1 == 'Bangers':
        if txtLength <= 5:
            namePDF.pdf.setFont(font1, 190)
            namePDF.pdf.scale(1, 1)
        elif 5 < txtLength <= 8:
            namePDF.pdf.setFont(font1, 190)
            namePDF.pdf.scale(0.9, 1)
        elif 8 < txtLength <= 10:
            namePDF.pdf.setFont(font1, 185)
            namePDF.pdf.scale(0.85, 1)
    elif font1 == 'Tough':
        if txtLength <= 5:
            namePDF.pdf.setFont(font1, 180)
            namePDF.pdf.scale(0.83, 1)
        elif 5 < txtLength <= 8:
            namePDF.pdf.setFont(font1, 185)
            namePDF.pdf.scale(0.6, 1)
        elif 8 < txtLength <= 10:
            namePDF.pdf.setFont(font1, 170)
            namePDF.pdf.scale(0.5, 1)
    elif font1 == 'College':
        if txtLength <= 5:
            namePDF.pdf.setFont(font1, 185)
            namePDF.pdf.scale(1.1, 1)
        elif 5 < txtLength <= 8:
            namePDF.pdf.setFont(font1, 175)
            namePDF.pdf.scale(0.8, 1)
        elif 8 < txtLength <= 10:
            namePDF.pdf.setFont(font1, 170)
            namePDF.pdf.scale(0.7, 1)
    elif font1 == 'Iceberg':
        if txtLength <= 5:
            namePDF.pdf.setFont(font1, 185)
            namePDF.pdf.scale(0.9, 1)
        elif 5 < txtLength <= 8:
            namePDF.pdf.setFont(font1, 175)
            namePDF.pdf.scale(0.7, 1)
        elif 8 < txtLength <= 10:
            namePDF.pdf.setFont(font1, 175)
            namePDF.pdf.scale(0.5, 1)
    elif font1 == 'Roboto':
        if txtLength <= 5:
            namePDF.pdf.setFont(font1, 190)
            namePDF.pdf.scale(0.9, 1)
        elif 5 < txtLength <= 8:
            namePDF.pdf.setFont(font1, 180)
            namePDF.pdf.scale(0.7, 1)
        elif 8 < txtLength <= 10:
            namePDF.pdf.setFont(font1, 175)
            namePDF.pdf.scale(0.55, 1)
    elif font1 == 'Sports Jersey':
        if txtLength <= 5:
            namePDF.pdf.setFont(font1, 185)
            namePDF.pdf.scale(1.1, 1)
        elif 5 < txtLength <= 8:
            namePDF.pdf.setFont(font1, 175)
            namePDF.pdf.scale(0.9, 1)
        elif 8 < txtLength <= 10:
            namePDF.pdf.setFont(font1, 170)
            namePDF.pdf.scale(0.68, 1)
    elif font1 == 'Asos':
        if txtLength <= 5:
            namePDF.pdf.setFont(font1, 170)
            namePDF.pdf.scale(.70, 1)
        elif 5 < txtLength <= 8:
            namePDF.pdf.setFont(font1, 165)
            namePDF.pdf.scale(.50,1)
        elif 8 < txtLength <= 10:
            namePDF.pdf.setFont(font1, 160)
            namePDF.pdf.scale(.35, 1)


def numberFontSize (num, font):
    numLength = len(num)
    if font == 'Jersey':
        if numLength == 1:
            namePDF.pdf.scale(1, 1)
            namePDF.pdf.setFont(font, 140)
        elif numLength == 2:
            namePDF.pdf.scale(.85, 1)
            namePDF.pdf.setFont(font, 160)
    elif font == 'College':
        namePDF.pdf.scale(.85, 1)
        namePDF.pdf.setFont(font, 160)
    elif font == 'Marker':
        namePDF.pdf.scale(.85, 1)
        namePDF.pdf.setFont(font, 160)
    elif font == 'Tough':
        namePDF.pdf.scale(.85, 1)
        namePDF.pdf.setFont(font, 160)
    elif font == 'Iceberg':
        namePDF.pdf.scale(.85, 1)
        namePDF.pdf.setFont(font, 160)
    elif font == 'Roboto':
        namePDF.pdf.scale(.85, 1)
        namePDF.pdf.setFont(font, 160)
    elif font == 'Asos':
        namePDF.pdf.scale(.85, 1)
        namePDF.pdf.setFont(font, 160)
    elif font == 'Adventure':
        namePDF.pdf.scale(.85, 1)
        namePDF.pdf.setFont(font, 160)
    elif font == 'Sporty':
        namePDF.pdf.scale(.85, 1)
        namePDF.pdf.setFont(font, 160)


def find_order(specific_order):
    x = 0
    while specific_order.upper() != "QUIT":
        if int(specific_order) == int(get_date.orders['orders'][x]['order_number']):
            product_id = int(get_date.orders['orders'][x]['line_items'][get_specificItem.number]["product_id"])
            print(product_id)
            # Custom Number Arm Sleeve
            if product_id == 626889097271:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                number = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][0]['value'])
                font = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][1]['value'])
                txt_color = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][2]['value'])
                size = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][3]['value'])
                print(f'''
                {name}
                {number}
                {font}
                {txt_color}
                {size}
                ''')
                namePDF.pdf.saveState()
                numberFontSize(number, font)
                namePDF.pdf.drawString(20, 1150 - (110*int(namePDF.numberEntries)), number)
                namePDF.pdf.restoreState()
                break
            # Customized Arm Sleeve
            elif product_id == 10834995656:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                text = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][0]['value'])
                font = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][1]['value'])
                txt_color = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][2]['value'])
                size = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][3]['value'])
                txt_length = len(text)
                print(f'''
                {name}
                {text}
                {font}
                {txt_color}
                {size}
                {txt_length}
                ''')
                namePDF.pdf.saveState()
                namePDF.pdf.scale(0.9, 1)
                namePDF.pdf.setFont(font, 125)
                namePDF.pdf.drawString(20, 1150 - (110*int(namePDF.numberEntries)), text)
                namePDF.pdf.restoreState()
                break
            # Custom Text Number Arm Sleeve
            elif product_id == 1421879279671:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                number = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][0]['value'])
                number_font = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][1]['value'])
                number_clr = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][2]['value'])
                txt = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][3]['value'])
                txt_font = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][4]['value'])
                txt_clr = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][5]['value'])
                size = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][6]['value'])
                def numOrTxt(answer):
                    if answer.upper() == 'BOTH':
                        # Number
                        namePDF.pdf.saveState()
                        namePDF.pdf.scale(0.9, 1)
                        namePDF.pdf.setFont(number_font, 125)
                        namePDF.pdf.drawString(700, 1150 - (110 * int(namePDF.numberEntries)), number)
                        namePDF.pdf.restoreState()
                        # Text
                        namePDF.pdf.saveState()
                        namePDF.pdf.scale(0.9, 1)
                        namePDF.pdf.setFont(txt_font, 125)
                        namePDF.pdf.drawString(20, 1150 - (110 * int(namePDF.numberEntries)), txt)
                        namePDF.pdf.restoreState()
                    elif answer.upper() == 'NUMBER':
                        #Number
                        namePDF.pdf.saveState()
                        namePDF.pdf.scale(0.9, 1)
                        namePDF.pdf.setFont(number_font, 125)
                        namePDF.pdf.drawString(700, 1150 - (110 * int(namePDF.numberEntries)), number)
                        namePDF.pdf.restoreState()
                    elif answer.upper() == 'TEXT':
                        # Text
                        namePDF.pdf.saveState()
                        namePDF.pdf.scale(0.9, 1)
                        namePDF.pdf.setFont(txt_font, 125)
                        namePDF.pdf.drawString(20, 1150 - (110 * int(namePDF.numberEntries)), txt)
                        namePDF.pdf.restoreState()
                #Showing option for text or Number
                label_NumOrTxt = tk.Label(text='Number or Txt: ')
                label_NumOrTxt.place(relx=.3, rely=.45)
                entry_NumOrTxt = tk.Entry(width=15)
                entry_NumOrTxt.place(relx=.55, rely=.45)
                button_NumOrTxt = tk.Button(text='Submit',
                                                command=lambda: numOrTxt(entry_NumOrTxt.get()))
                button_NumOrTxt.place(relx=.4, rely=.5)
                print(f'''
                {name}
                Number: {number}
                Number Font: {number_font}
                Number Color: {number_clr}
                Text: {txt}
                Text Font: {txt_font}
                Text Color: {txt_clr}
                Size: {size}
                ''')
                break
            #Custom Headband
            elif product_id == 1376623132727:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                txt = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][0]['value'])
                font = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][1]['value'])
                txt_color = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][2]['value'])
                size = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][3]['value'])
                print(f'''
                {name}
                {txt}
                {font}
                {txt_color}
                {size}
                ''')
                namePDF.pdf.saveState()
                headbandFontSize(txt, font)
                namePDF.pdf.drawString(20, 1150 - (150*int(namePDF.numberEntries)), txt)
                namePDF.pdf.restoreState()
                break
            #H2O Dry Tek
            elif product_id == 4449171472439:
                print('Item is H20 Drytek')
                break
            #Number Football Towel
            elif product_id == 1688836046903:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                number = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][0]['value'])
                font = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][1]['value'])
                txt_color = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][2]['value'])
                print(f'''
                {name}
                {number}
                {font}
                {txt_color}
                ''')
                namePDF.pdf.saveState()
                numberFontSize(number, font)
                namePDF.pdf.drawString(20, 1150 - (110*int(namePDF.numberEntries)), number)
                namePDF.pdf.restoreState()
                break
            #Custom Leg Sleeve
            elif product_id == 673478279223:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                text = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][0]['value'])
                font = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][1]['value'])
                txt_color = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][2]['value'])
                size = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][3]['value'])
                txt_length = len(text)
                print(f'''
                    {name}
                    {text}
                    {font}
                    {txt_color}
                    {size}
                    {txt_length}
                    ''')
                namePDF.pdf.saveState()
                namePDF.pdf.scale(0.9, 1)
                namePDF.pdf.setFont(font, 125)
                namePDF.pdf.drawString(20, 1150 - (110 * int(namePDF.numberEntries)), text)
                namePDF.pdf.restoreState()
                break
            #Trust God
            elif product_id == 4449409925175:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                print(f'''
                {name}
                ''')
                namePDF.pdf.drawImage('trust god.png', 10, 1125 - (110 * int(namePDF.numberEntries)), width=600, preserveAspectRatio=True, mask='auto')
                break
            #Why So Serious
            elif product_id == 1460221837367:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                print(name)
                namePDF.pdf.drawImage('why-so-serious.png', 10, 1075 - (110 * int(namePDF.numberEntries)), width=625,
                                      preserveAspectRatio=False, mask='auto', height=225)
                break
            #For momma
            elif product_id == 4449405599799:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                print(name)
                namePDF.pdf.drawImage('for-momma.png', 10, 1150 - (110 * int(namePDF.numberEntries)), width=625,
                                      preserveAspectRatio=False, mask='auto', height=120)
                break
            #Goat
            elif product_id == 1460206665783:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                print(name)
                namePDF.pdf.drawImage('goat.png', 10, 1150 - (110 * int(namePDF.numberEntries)), width=625,
                                      preserveAspectRatio=False, mask='auto', height=120)
                break
            #Sauce
            elif product_id == 1460211646519:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                print(name)
                namePDF.pdf.drawImage('saucepng.png', 10, 1090 - (110 * int(namePDF.numberEntries)), width=625,
                                      preserveAspectRatio=False, mask='auto', height=180)
                break
            #Custom Forearm
            elif product_id == 1386165796919:
                name = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['name'])
                right_txt = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][0]['value'])
                left_txt = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][1]['value'])
                font = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][2]['value'])
                font_clr = (get_date.orders['orders'][x]['line_items'][get_specificItem.number]['properties'][3]['value'])
                print(f'''
                {name}
                Right txt: {right_txt}
                Left txt: {left_txt}
                Font: {font}
                Font Clr: {font_clr}''')
                #Right Text
                namePDF.pdf.saveState()
                namePDF.pdf.scale(0.7, 1)
                namePDF.pdf.setFont(font, 125)
                namePDF.pdf.drawString(20, 1150 - (110 * int(namePDF.numberEntries)), right_txt)
                namePDF.pdf.restoreState()
                namePDF.numberEntries = namePDF.numberEntries + 1
                #Left Text
                namePDF.pdf.saveState()
                namePDF.pdf.scale(0.7, 1)
                namePDF.pdf.setFont(font, 125)
                namePDF.pdf.drawString(20, 1150 - (110 * int(namePDF.numberEntries)), left_txt)
                namePDF.pdf.restoreState()
                break
            else:
                print('Item not valid')
                break
        else:
            x = x + 1
    namePDF.numberEntries = namePDF.numberEntries + 1


def savePDF():
    namePDF.pdf.save()


def get_specificItem(number):
    get_specificItem.number = number
    get_specificItem.number = int(get_specificItem.number)

#Get Date for API-------------------------------------------------------
label_date = tk.Label(text='Date: ')
label_date.place(relx=.05, rely=.08)

entry_date = tk.Entry(width=15)
entry_date.place(relx=.09, rely=.076)

button_date = tk.Button(text='Get Order Info', command=lambda: get_date())
button_date.place(relx=.20, rely=.076)

#Name PDF----------------------------------------------------------------
label_pdf = tk.Label(text='PDF NAME: ')
label_pdf.place(relx=.032, rely=.12)

entry_pdf = tk.Entry(width=15)
entry_pdf.place(relx=.09, rely=.117)

button_pdf = tk.Button(text='Name PDF', command=lambda: namePDF(entry_pdf.get()))
button_pdf.place(relx=.20, rely=.117)

#Select Order Number----------------------------------------------------
label_order = tk.Label(text='Order Number: ')
label_order.place(relx=.020, rely=.16)

entry_order = tk.Entry(width=15)
entry_order.place(relx=.09, rely=.158)

button_order = tk.Button(text='Get Order Info', command=lambda: find_order(entry_order.get()))
button_order.place(relx=.20, rely=.158)

#Save PDF---------------------------------------------------------------
button_savePDF = tk.Button(text='Save PDF', command=lambda: savePDF())
button_savePDF.place(relx=.40, rely=.6)

#Get Specific Item------------------------------------------------------
label_specificItem = tk.Label(text='Line Number:')
label_specificItem.place(relx=.02, rely=.2)

entry_specificItem = tk.Entry(width=15)
entry_specificItem.place(relx=.09, rely=.199)

button_specificItem = tk.Button(text='Get Line Item', command=lambda: get_specificItem(entry_specificItem.get()))
button_specificItem.place(relx=.2, rely=.199)

#lists for sorting-------------------------------------------------------
white_list = []
black_list = []
navy_list = []
pink_list = []
shark_teal_list = []
carolina_blue_list = []
royal_blue_list = []
athletic_yellow_list = []
bright_yellow_list = []
kelly_green_list = []
forest_green_list = []
hi_vis_green_list = []
vegas_gold_list = []
shiny_gold_list = []
shiny_silver_list = []
brown_list = []
midnight_navy_list = []
purple_list = []
maroon_list = []
red_list = []
sport_orange_list = []
no_customization_list = []

#functions for sorting orders-------------------------------------------------------------------------------------------

def add_to_list(txt_color, specific_order, line_number):
    if txt_color == 'White':
        white_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Black':
        black_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Navy':
        navy_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Pink':
        pink_list.append(f'{specific_order}, {line_number}')
    elif txt_color == "Carolina Blue":
        carolina_blue_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Royal Blue':
        royal_blue_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Shark Teal':
        shark_teal_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Midnight Navy':
        midnight_navy_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Sport Orange':
        sport_orange_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Purple':
        purple_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Brown':
        brown_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Maroon':
        maroon_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Red':
        red_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Shiny Silver':
        shiny_silver_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Shiny Gold':
        shiny_gold_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Vegas Gold':
        vegas_gold_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'High-Vis Green':
        hi_vis_green_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Forest Green':
        forest_green_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Kelly Green':
        kelly_green_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Bright Yellow':
        bright_yellow_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 'Athletic Yellow':
        athletic_yellow_list.append(f'{specific_order}, {line_number}')
    elif txt_color == 0:
        no_customization_list.append(f'{specific_order}, {line_number}')


def find_range(start, end):
    return list(range(start, end + 1, 1))


def text_1(number_of_items, x2, specific_order):
    x1 = 0
    while x1 < number_of_items:
        product_id = int(get_date.orders['orders'][x2]['line_items'][x1]["product_id"])
        # Custom Number Product-----------------------------------------------------------------------------------------
        if product_id == 626889097271:
            txt_color = (get_date.orders['orders'][x2]['line_items'][x1]['properties'][2]['value'])
            print(txt_color)
            add_to_list(txt_color, specific_order, x1)
        # Customized Arm Sleeve-----------------------------------------------------------------------------------------
        elif product_id == 10834995656:
            txt_color = (
                get_date.orders['orders'][x2]['line_items'][x1]['properties'][2]['value'])
            print(txt_color)
            add_to_list(txt_color, specific_order, x1)
        # Custom Text Number Sleeve-------------------------------------------------------------------------------------
        elif product_id == 1421879279671:
            number_clr = (
                get_date.orders['orders'][x2]['line_items'][x1]['properties'][2]['value'])
            add_to_list(number_clr, specific_order, x1)
            txt_clr = (
                get_date.orders['orders'][x2]['line_items'][x1]['properties'][5]['value'])
            add_to_list(txt_clr, specific_order, x1)
        # Custom Headband-----------------------------------------------------------------------------------------------
        elif product_id == 1376623132727:
            txt_color = (
                get_date.orders['orders'][x2]['line_items'][x1]['properties'][2]['value'])
            add_to_list(txt_color, specific_order, x1)
        # Custom Leg Sleeve---------------------------------------------------------------------------------------------
        elif product_id == 673478279223:
            txt_color = (
                get_date.orders['orders'][x2]['line_items'][x1]['properties'][2]['value'])
            add_to_list(txt_color, specific_order, x1)
        # Custom Forearm------------------------------------------------------------------------------------------------
        elif product_id == 1386165796919:
            font_clr = (
                get_date.orders['orders'][x2]['line_items'][x1]['properties'][3]['value'])
            add_to_list(font_clr, specific_order, x1)
        #Custom Football Towel------------------------------------------------------------------------------------------
        elif product_id == 1688836046903:
            txt_color = (get_date.orders['orders'][x2]['line_items'][get_specificItem.number]['properties'][2]['value'])
            add_to_list(txt_color, specific_order, x1)
        else:
            add_to_list(0, specific_order, x1)
        x1 = x1 + 1


def filter_order_text_color(specific_order):
    x2 = 0
    while specific_order != "QUIT":
        if specific_order == int(get_date.orders['orders'][x2]['order_number']):
            print(specific_order)
            number_of_items = int(len(get_date.orders['orders'][x2]['line_items']))
            print(number_of_items)
            text_1(number_of_items, x2, specific_order)
            break
        else:
            x2 = x2 + 1


def print_lists():
    print("White: " + str(white_list))
    print('Black: ' + str(black_list))
    print('Navy: ' + str(navy_list))
    print('Pink: ' + str(pink_list))
    print('Shark Teal: ' + str(shark_teal_list))
    print('Carolina Blue: ' + str(carolina_blue_list))
    print('Royal Blue: ' + str(royal_blue_list))
    print('Athletic Yellow: ' + str(athletic_yellow_list))
    print('Bright Yellow: ' + str(bright_yellow_list))
    print('Kelly Green: ' + str(kelly_green_list))
    print('Forest Green: ' + str(forest_green_list))
    print('HI VIS Green: ' + str(hi_vis_green_list))
    print('Vegas Gold: ' + str(vegas_gold_list))
    print('Shiny Gold: ' + str(shiny_gold_list))
    print('Shiny Silver: ' + str(shiny_silver_list))
    print('Brown: ' + str(brown_list))
    print('Midnight Navy: ' + str(midnight_navy_list))
    print('Purple: ' + str(purple_list))
    print('Maroon: ' + str(maroon_list))
    print('Red: ' + str(red_list))
    print('Sport Orange: ' + str(sport_orange_list))
    print('No Customization: ' + str(no_customization_list))
    white_label = tk.Label(text=f'{white_list}')
    white_label.place(relx=.5, rely=.4)


def sort_orders(beg_num, end_num):
    list1 = find_range(beg_num, end_num)
    print(list1)
    range = len(find_range(beg_num, end_num))
    y1 = 0
    while y1 < range:
        filter_order_text_color(list1[y1])
        y1 = y1 + 1
    print_lists()
    print(white_list[0][0])




#Beginning Number tkinter-----------------------------------------------------
label_beginning_number = tk.Label(text="Beginning Order Number: ")
label_beginning_number.place(relx=.5, rely=.2)

entry_beginning_number = tk.Entry(width=15)
entry_beginning_number.place(relx=.62, rely=.195)

#Ending Number tkinter---------------------------------------------------------
label_ending_number = tk.Label(text="Ending Order Number: ")
label_ending_number.place(relx=.5, rely=.25)

entry_ending_number = tk.Entry(width=15)
entry_ending_number.place(relx=.62, rely=.25)

#Button for making sorting------------------------------------------------------
button_sort_orders = tk.Button(text="Sort Orders", command=lambda: sort_orders(int(entry_beginning_number.get()), int(entry_ending_number.get())))
button_sort_orders.place(relx=.62, rely=.3)

root.mainloop()