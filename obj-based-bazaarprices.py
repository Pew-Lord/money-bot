import requests, ujson

data = requests.get("https://api.hypixel.net/skyblock/bazaar",  timeout=10).json()
data = data['products']

class Items:
    def __init__(self, id, sell, buy)
    self.id = id
    self.sell = sell
    self.buy = buy

    def price(self):
        return buy
    def value(self):
        return sell
for i in data:
    tempid = ""
    tempsell = float
    tempbuy = float

'''
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


itembuypriceprice = []
for i in data:
    try:
        x = data[i]
        y = x["sell_summary"]
        z = y[0]
        itembuypriceprice.append(z["pricePerUnit"])
    except IndexError:
        itembuypriceprice.append(-1)
        pass

itemsellprice = []
for i in data:
    try:
        x = data[i]
        y = x["buy_summary"]
        z = y[0]
        itemsellprice.append(z["pricePerUnit"])
    except IndexError:
        itemsellprice.append(-1)
        pass

buyorderprice = {}
sellorderprice = {}

for i in range(len(items)):
    buyorderprice[items[i]] = itembuypriceprice[i]

for i in range(len(items)):
    sellorderprice[items[i]] = itemsellprice[i]

for i in range(len(items)):
    if not ":" in items[i]:
        continue
    #print(items[i])
'''