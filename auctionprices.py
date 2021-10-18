import requests, ujson, datetime
starttime = datetime.datetime.now()

data = requests.get("https://api.hypixel.net/skyblock/auctions").json()

class Items:
    def __init__(self, name, price, uuid):
        self.name = name
        self.price = price
        self.uuid = uuid
auctions = []
for i in range(data["totalPages"]):
    data = requests.get("https://api.hypixel.net/skyblock/auctions?page={}".format(i)).json()
    data = data["auctions"]
    for j in range(len(data)):
        k = data[j]
        try:
            k["bin"]
        except KeyError:
            continue
        if k["item_name"] == "Enchanted Book":
            continue
        auctions.append(Items(k["item_name"], k["starting_bid"], k["uuid"]))

itemsremoved = 0
for i in range(len(auctions)):
    i = i - itemsremoved
    itemname = auctions[i].name
    if "[" in itemname:
        auctions.pop(i)
        itemsremoved += 1



def takePrice(array):
    return array[1]
def getitemprice(item_name):
    '''

    :param item_name: (str)
    :return: (str) (str) (str)
    '''
    items2 = []
    for x in range(len(auctions)):
        item = auctions[x].name
        if item_name.lower() in item.lower():
            items2.append((auctions[x].name, auctions[x].price, auctions[x].uuid))
        items2.sort(key=takePrice)
    try:
        npu = items2[0]
    except IndexError:
        return "N/A", "-1", "N/A"
    
    npu = (npu[0], ("{:,}".format(npu[1])), npu[2])
    return npu[0], npu[1], npu[2]
    return "The cheapest {} is {}, you can look at the auction with the command /viewauction {}".format(npu[0], npu[1], npu[2])


if __name__ == "__main__":
    print(getitemprice("Hyperion"))
    print(datetime.datetime.now() - starttime)
