# all code within this file is made by Lord#0427 on discord, unless otherwise mentioned.
import requests, ujson # i did not make these modules

data = requests.get("https://api.hypixel.net/skyblock/bazaar",  timeout=10).json() # i have no affiliation with hypixel
data = data['products']

class Items:
    def __init__(self, id, name, sell, buy):
        self.id = id
        self.name = name
        self.sell = sell
        self.buy = buy

    def price(self):
        return self.buy
    def value(self):
        return self.sell
    def myname(self):
        return self.id
iter = 0
items = []
def nameCleaner(name):
    '''
    returns the name, but cleaner
    :param name: (str)
    :return: (str)
    '''
    templist = []
    name = name.replace("_", " ")
    name = name.lower()
    name = name.split()
    for x in name:
        x = x.capitalize()
        templist.append(x)
    
    temp = " ".join(templist)
    return temp
for i in data:
    temp = ""
    templist = []
    i = i.replace("_", " ")
    i = i.lower()
    i = i.split()
    for x in i:
        x = x.capitalize()
        templist.append(x)
    
    temp = " ".join(templist)
    items.append(temp)
items2 = []
for i in range(len(items)):
    items2.append(items[i])
for i in data:
    j = data[i]
    k = j["buy_summary"]
    l = j["sell_summary"]
    try:
        m = k[0]
        tempsell = m["pricePerUnit"]
    except IndexError:
        tempsell = -1
    try:
        n = l[0]
        tempbuy = n["pricePerUnit"]
    except IndexError:
        tempbuy = -1
    tempid = nameCleaner(j["product_id"])
    tempname = tempid
    items2[iter] = Items(tempid, tempname, tempsell, tempbuy)
    iter += 1

def updatePrices():
    data = requests.get("https://api.hypixel.net/skyblock/bazaar",  timeout=10).json()
    data = data["products"]
    upiter = 0
    for i in data:
        j = data[i]
        k = j["buy_summary"]
        l = j["sell_summary"]
        try:
            m = k[0]
            tempsell = m["pricePerUnit"]
        except IndexError:
            tempsell = -1
        try:
            n = l[0]
            tempbuy = n["pricePerUnit"]
        except IndexError:
            tempbuy = -1
        items2[upiter].sell = tempsell
        items2[upiter].buy = tempbuy
        upiter += 1