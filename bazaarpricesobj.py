import requests, ujson

data = requests.get("https://api.hypixel.net/skyblock/bazaar",  timeout=10).json()
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
iter = 0
items = []
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
    tempid = j["product_id"]
    tempname = tempid
    items2[iter] = Items(tempid, tempname, tempsell, tempbuy)
    iter += 1