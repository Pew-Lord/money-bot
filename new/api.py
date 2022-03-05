# All code within this file was written by Lord#0427 on discord.
import requests, ujson

# --- BAZAAR --- #

def clean(name):
    """
    cleans the item name
    :param name: (str)
    :return: (str)
    """
    if ":" in name:
        return name
    name = name.lower().replace("_", " ").split()
    for i in range(len(name)-1, -1, -1):
        if name[i] == "item": # regular carrot is called "carrot item", same with potato. this fixes that
            name.pop(i)
            continue
        name[i] = name[i].capitalize()
    return " ".join(name)

def getBazaarInfo():
    """
    gets the bazaar information from the api
    :return: (list)
    """

    data = requests.get("https://api.hypixel.net/skyblock/bazaar", timeout=10).json() # gets the data from the api
    data = data["products"] # essentially zooms in, getting rid of a layer

    data_list = [] # format: formatted name, id, buy price, sell price
    for ele in data:
        if ele in ["BAZAAR_COOKIE"]:
            continue
        name = ele
        name = clean(name)
        data_list.append((name, ele, round(data[ele]["quick_status"]["sellPrice"], 1), round(data[ele]["quick_status"]["buyPrice"], 1)))
    return data_list

def indexBazaar():
    data = getBazaarInfo()
    for ele in data:
        if "Carrot" in ele[0]:
            print(ele)

# --- AUCTION HOUSE --- #

def username(ID):
    """
    turns the user id into a username
    :param ID: (str)
    :return: (str)
    """
    name = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{ID}", timeout=10).json()
    name = name["name"]
    return name

def getAuctions():
    """
    gets the auction house information (BIN only)
    :return: (list)
    """

    data = requests.get("https://api.hypixel.net/skyblock/auctions", timeout=10).json() # to get page number
    pages = data["totalPages"]
    auctions = []
    for page in range(pages):
        data = requests.get(f"https://api.hypixel.net/skyblock/auctions?page={page}", timeout=10).json()
        time = data["lastUpdated"]
        data = data["auctions"]
        for ele in data:
            if ele["bin"] == False: # sorting our auctions, leaving BIN
                continue
            if ele["end"] < time: # sorting out expired auctions
                continue
            if ele["item_name"] == "Enchanted Book": # sorting out enchanted books because they're annoying
                continue
            auctions.append((ele["item_name"], ele["starting_bid"], ele["auctioneer"], ele["uuid"]))
    return auctions



auctions = getAuctions()
