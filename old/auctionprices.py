# all code within this file is made by Lord#0427 on discord, unless otherwise mentioned.
import requests, ujson # I did not make these modules

def takeSecond(array):
    '''
    Takes the 2nd value of an array
    :param array: (array)
    :return: (str)
    '''
    return array[1]
def ahPrice(item_name):
    '''
    Gets the current cheapest price of an item in Hypixel Skyblock
    :param item_name: (str)
    :return: (str) (str) (str)
    '''
    data = requests.get("https://api.hypixel.net/skyblock/auctions").json() # I have no affiliation with Hypixel
    class Items:
        def __init__(self, name, price, uuid):
            self.name = name
            self.price = price
            self.uuid = uuid
    auctions = []
    for i in range(data["totalPages"]):
        data = requests.get("https://api.hypixel.net/skyblock/auctions?page={}".format(i)).json() # I have no affiliation with Hypixel.
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
        items2 = []
        for x in range(len(auctions)):
            item = auctions[x].name
            if item_name.lower() in item.lower():
                items2.append((auctions[x].name, auctions[x].price, auctions[x].uuid))
            items2.sort(key=takeSecond)
        try:
            npu = items2[0]
        except IndexError:
            return "N/A", "-1", "N/A"
        
        npu = (npu[0], ("{:,}".format(npu[1])), npu[2])
        return npu[0], npu[1], npu[2]
