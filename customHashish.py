# make a hashmap of all the custom items, the key will be the productIDs and the data will be what to do when you find that
# specific item
#list of product IDs
prodIDs = [10834995656, 1421879279671, 10834995656, 626889097271] # <-- put them in there

"""
10834995656 - 
1421879279671 - 
10834995656 - text, font, txt_color
626889097271 - number, font, txt_color

"""
#1421879279671 - customized text number sleeve
#10834995656 - customized arm sleeve

# 10834995656 = ["Color*", "Text", "Choose Font", "Choose a Color", "Size*"]

listOfColorLists = {}

listOfColorLists["White"] = []
listOfColorLists["Black"] = []
listOfColorLists["Red"] = []
listOfColorLists["Blue"] = []


class textData:
    text = ""
    font = ""

    def textData(self):
        self.text = ""
        self.font = ""

    def setText(self, data):
        self.text = data

    def getText(self):
        return self.text

    def setFont(self, data):
        self.font = data
    
    def getFont(self):
        return self.font
"""
PushDataToList
    - 
Parameter:
    - Input: 
"""
def pushDataToList(text, color, font):
    myTextData = textData()
    myTextData.textData()
    myTextData.setText(text)
    myTextData.setFont(font)
    if color in listOfColorLists:
        listOfColorLists[color].append(myTextData)
    else:
        print("color not found")

def getDataFromLineItem(productID, item):

    def customPick(x):
        return item["properties"][x]["value"]

    #Custom Number
    print(productID)
    print(type(productID))
    if(productID == 626889097271):
        number = customPick(0)
        font = customPick(1)
        textColor = customPick(2)
        print("inside custom Number")
        pushDataToList(number, textColor, font)

    #Customized Arm Sleeve
    elif(productID == 10834995656):
        text = item["properties"][0]["value"]
        font = customPick(1)
        textColor = customPick(2)
        textLength = customPick(3)
        pushDataToList(text, textColor, font)

    #Custom Text Number
    elif(productID == 1421879279671):
        number = customPick(0)
        numberFont = customPick(1)
        numberColor = customPick(2)
        text = customPick(3)
        textFont = customPick(4)
        textColor = customPick(5)
        pushDataToList(text, textColor, textFont)
        pushDataToList(number, numberColor, numberFont)

    #Custom Headband
    elif(productID == 1376623132727):
        text = customPick(0)
        font = customPick(1)
        textColor = customPick(2)
        pushDataToList(text, textColor, font)

    # Number Football Towel
    elif(productID == 1688836046903):
        number = customPick(1)
        

    #Custom Leg Sleeve
    elif(productID == 673478279223):
        text = customPick(0)
        font = customPick(1)
        textColor = customPick(2)
        pushDataToList(text, textColor, font)
    
    else:
        print("Not a Custom Item")