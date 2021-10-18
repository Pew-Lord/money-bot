import requests, ujson

data = requests.get("https://api.hypixel.net/skyblock/auctions", timeout=10).json()
print(data["page"])
data = data["auctions"]
'''
x = data[0]
print(x["item_name"])
'''
auctions = []
for i in range(len(data)):
    j = data[i]
    if j["item_name"] == "Enchanted Book":
        continue
    temp = (j["item_name"], j["starting_bid"])
    auctions.append(temp)


def takeSecond(ele):
    return ele[1]
auctions.sort(reverse=True, key=takeSecond)
