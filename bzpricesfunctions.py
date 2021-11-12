# all code within this file is made by Lord#0427 on discord, unless otherwise mentioned.
import bazaarpricesobj as bzobj
from math import floor

def itemnames():
    '''
    returns the name of every item (putting the exact text written for an item will trigger
    commands (eg. $price ____))
    :return: (str) (str) (str) (str) (str)
    '''
    seglen = int
    leftover = int
    iter = 0
    rotations = 4
    rotation = []
    index = 0
    returns = []
    str = ""

    if len(bzobj.items) / 4 != int:
        seglen = len(bzobj.items) // 4
        leftover = len(bzobj.items) - (4 * seglen)
    else:
        seglen = (len(bzobj.items) / 4)
    while rotations > 0:
        while iter < seglen:
            rotation.append(bzobj.items[index])
            index += 1
            iter += 1
        iter = 0
        rotations -= 1
        str = ", ".join(rotation)
        rotation = []
        returns.append(str)
        str = ""
    if len(bzobj.items) > (4 * seglen):
        iter = seglen * 4
        while len(bzobj.items) >= (iter - 1):
            rotation.append(bzobj.items[index])
            index += 1
            iter += 1
        str = ", ".join(rotation)
        returns.append(str)
    if len(returns) != 4:
        return returns[0], returns[1], returns[2], returns[3], returns[4]
    else:
        return returns[0], returns[1], returns[2], returns[3], ""
def itemprices():
    '''
    returns the name and price of every item
    :return: (str) (str) (str) (str) (str) (str) (str) (str) (str)
    '''
    rotations = 8
    iterations = len(bzobj.items) // 8
    totaliters = 0
    list = []
    returns = []
    if len(bzobj.items) / 8 != (8*iterations):
        leftover = len(bzobj.items) - (8*iterations)
    while rotations > 0:
        for i in range(iterations):
            x = "({}:{})".format((bzobj.items2[totaliters].myname()), str((bzobj.items2[totaliters].price())))
            list.append(x)
            totaliters += 1
        rstring = ", ".join(list)
        list = []
        returns.append(rstring)
        rotations -= 1
    if leftover != 0:
        while totaliters <= (len(bzobj.items)):
            x = "({}:{})".format((bzobj.items2[totaliters].myname()), str((bzobj.items2[totaliters].price())))
            list.append(x)
            totaliters += 1
        rstring = ", ".join(list)
        returns.append(rstring)
    else:
        returns.append("")
    return returns[0], returns[1], returns[2], returns[3], returns[4], returns[5], returns[6], returns[7], returns[8]
def itemvalues():
    '''
    returns the name and value of every item
    :return: (str) (str) (str) (str) (str) (str) (str) (str) (str)
    '''
    rotations = 8
    iterations = len(bzobj.items) // 8
    totaliters = 0
    list = []
    returns = []
    if len(bzobj.items) / 8 != (8*iterations):
        leftover = len(bzobj.items) - (8*iterations)
    while rotations > 0:
        for i in range(iterations):
            x = "({}:{})".format((bzobj.items2[totaliters].myname()), str((bzobj.items2[totaliters].value())))
            list.append(x)
            totaliters += 1
        rstring = ", ".join(list)
        list = []
        returns.append(rstring)
        rotations -= 1
    if leftover != 0:
        while totaliters <= (len(bzobj.items)):
            x = "({}:{})".format((bzobj.items2[totaliters].myname()), str((bzobj.items2[totaliters].value())))
            list.append(x)
            totaliters += 1
        rstring = ", ".join(list)
        returns.append(rstring)
    else:
        returns.append("")
    return returns[0], returns[1], returns[2], returns[3], returns[4], returns[5], returns[6], returns[7], returns[8]
def specificitemprice(item_name):
    '''
    returns the price of a specific item
    :param item_name: (str)
    :return: (float)
    '''
    item_name = item_name.split()
    templist = []
    for x in item_name:
        x = x.capitalize()
        templist.append(x)
    item_name = " ".join(templist)
    return bzobj.items2[bzobj.items.index(item_name)].price()
def specificitemvalue(item_name):
    '''
    returns the value of a specific item
    :param item_name: (str)
    :return: (float)
    '''
    item_name = item_name.split()
    templist = []
    for x in item_name:
        x = x.capitalize()
        templist.append(x)
    item_name = " ".join(templist)
    return bzobj.items2[bzobj.items.index(item_name)].value()


def goldenTooth(MONEY):
    MONEY = MONEY / 10000
    MONEY = floor(MONEY)
    MONEY = MONEY * 10000
    GT = specificitemvalue("Golden Tooth")
    WT = specificitemprice("Wolf Tooth")
    EG = specificitemprice("Enchanted Gold")
    AMOUNT = 0
    GT = GT / 100
    GT = floor(GT)
    GT = GT * 100
    WT = WT / 100
    WT = round(WT, 1)
    WT = WT * 100
    EG = EG / 100
    EG = round(EG, 1)
    EG = EG * 100
    WT = WT * 128
    EG = EG * 32
    PROFIT = GT - (EG + WT)
    TOTALCOST = EG + WT
    while True:
        if not MONEY <= TOTALCOST * (1 + AMOUNT):
            AMOUNT += 1
            continue
        break
    return (128 * AMOUNT, 32 * AMOUNT, AMOUNT, PROFIT * AMOUNT)


if __name__ == "__main__":
    print(goldenTooth(2320000))