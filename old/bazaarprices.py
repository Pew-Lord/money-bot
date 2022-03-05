# all code within this file is made by Lord#0427 on discord, unless otherwise mentioned.
import requests, ujson # i did not make these modules

data = requests.get("https://api.hypixel.net/skyblock/bazaar",  timeout=10).json() # i have no affiliation with hypixel
data = data['products']
items = []
templen = 0
templen2 = []
for i in data:
    temp = ""
    templist = []
    i = i.replace("_", " ")
    i = i.lower()
    i = i.split()
    for x in i:
        x = x.capitalize()
        if len(i) > templen:
            templen = len(i)
            templen2 = i

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

#print(buyorderprice["Raw Fish:3"])
#print(sellorderprice["Raw Fish:3"])
print(buyorderprice["Enchanted Carrot On A Stick"])
print(sellorderprice["Enchanted Carrot On A Stick"])
wierdItems = {
    "Log 2:1": "Dark Oak Wood",
    "Log:1": "Spruce Wood",
    "Log:2":"Birch Wood",
    "Log:3":"Jungle Wood",
    "Raw Fish:1":"Raw Salmon",
    "Raw Fish:2":"ClownFish",
    "Raw Fish:3":"",
    "":"",
    "":""

}
'''
Ink Sack:3
Ink Sack:4
Raw Fish:3
Raw Fish:2
Raw Fish:1
'''
'''
for i in items:
    if ":" in i:
        iter += 1
print(iter)
'''
'''
sell_summary = buy order
buy_summary = sell order
'''
