# all code within this file is made by Lord#0427 on discord, unless otherwise mentioned.
import bazaarpricesobj as bzobj
from math import floor

def itemnames():
    '''
    returns the name of every item (putting the exact text written for an item will trigger
    commands (eg. $price ____))
    :return: (str) (str) (str) (str) (str)
    '''
    bzobj.updatePrices()
    seglen = int
    leftover = int
    iter = 0
    rotations = 4
    rotation = []
    index = 0
    returns = []
    str = ""

    if len(bzobj.items) % 4 != 0:
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

def newItems():
    """
    New function (replacing itemnames())
    :return: (str) (str) (str) (str) (str)
    """
    bzobj.updatePrices()
    items = []
    sublist = []
    segmentlength = 0
    SL2 = 0
    segmentstart = 0
    if len(bzobj.items) % 4 == 0:
        segmentlength = int(len(bzobj.items) / 4)
        SL2 = segmentlength
        for i in range(4):
            for i in range(segmentstart, SL2):
                sublist.append(bzobj.items[i])
            segmentstart += segmentlength
            SL2 += segmentlength
            sublist = ", ".join(sublist)
            items.append(sublist)
            sublist = []
    else:
        extras = len(bzobj.items) % 4
        segmentlength = int((len(bzobj.items)-extras) / 4)
        SL2 = segmentlength
        for i in range(4):
            for i in range(segmentstart, SL2):
                sublist.append(bzobj.items[i])
            if i != 3:
                segmentstart += segmentlength
                SL2 += segmentlength
            sublist = ", ".join(sublist)
            items.append(sublist)
            sublist = []
        segmentstart += segmentlength
        segmentstart = 4 * segmentlength
        SL2 = segmentstart + extras
        for i in range(segmentstart, SL2):
            sublist.append(bzobj.items[i])
        items.append(", ".join(sublist))
    if len(items) == 4:
        return items[0], items[1], items[2], items[3], ""
    else:
        return items[0], items[1], items[2], items[3], items[4]

def newPrices():
    """
    new function to replace itemprices()
    :return: (str) (str) (str) (str) (str) (str) (str) (str) (str)
    """
    bzobj.updatePrices()
    items = []
    sublist = []
    segmentlength = 0
    SL2 = 0
    segmentstart = 0
    if len(bzobj.items) % 8 == 0:
        segmentlength = int(len(bzobj.items) / 8)
        SL2 = segmentlength
        for i in range(8):
            for i in range(segmentstart, SL2):
                sublist.append(("{}; {}".format(bzobj.items[i], bzobj.items2[i].price())))
            segmentstart += segmentlength
            SL2 += segmentlength
            sublist = ", ".join(sublist)
            items.append(sublist)
            sublist = []
    else:
        extras = len(bzobj.items) % 8
        segmentlength = int((len(bzobj.items)-extras) / 8)
        SL2 = segmentlength
        for i in range(8):
            for i in range(segmentstart, SL2):
                sublist.append(("{}; {}".format(bzobj.items[i], bzobj.items2[i].price())))
            if i != 7:
                segmentstart += segmentlength
                SL2 += segmentlength
            sublist = ", ".join(sublist)
            items.append(sublist)
            sublist = []
        segmentstart += segmentlength
        segmentstart = 8 * segmentlength
        SL2 = segmentstart + extras
        for i in range(segmentstart, SL2):
            sublist.append(("{}; {}".format(bzobj.items[i], bzobj.items2[i].price())))
        items.append(", ".join(sublist))
    if len(items) == 8:
        return items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], ""
    else:
        return items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8]

def newValues():
    """
    new function (replacing itemvalues())
    :return: (str) (str) (str) (str) (str)(str)(str) (str) (str)
    """
    bzobj.updatePrices()
    items = []
    sublist = []
    segmentlength = 0
    SL2 = 0
    segmentstart = 0
    if len(bzobj.items) % 8 == 0:
        segmentlength = int(len(bzobj.items) / 8)
        SL2 = segmentlength
        for i in range(8):
            for i in range(segmentstart, SL2):
                sublist.append(("{}; {}".format(bzobj.items[i], bzobj.items2[i].value())))
            segmentstart += segmentlength
            SL2 += segmentlength
            sublist = ", ".join(sublist)
            items.append(sublist)
            sublist = []
    else:
        extras = len(bzobj.items) % 8
        segmentlength = int((len(bzobj.items)-extras) / 8)
        SL2 = segmentlength
        for i in range(8):
            for i in range(segmentstart, SL2):
                sublist.append(("{}; {}".format(bzobj.items[i], bzobj.items2[i].value())))
            if i != 7:
                segmentstart += segmentlength
                SL2 += segmentlength
            sublist = ", ".join(sublist)
            items.append(sublist)
            sublist = []
        segmentstart += segmentlength
        segmentstart = 8 * segmentlength
        SL2 = segmentstart + extras
        for i in range(segmentstart, SL2):
            sublist.append(("{}; {}".format(bzobj.items[i], bzobj.items2[i].price())))
        items.append(", ".join(sublist))
    if len(items) == 8:
        return items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], ""
    else:
        return items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8]

def profit(item_name):
    """
    gets the sell price and buy price of an item, and returns the profit you can make on an item
    :param item_name: (str)
    :return: (float)
    """
    bzobj.updatePrices()
    itemindex = 0
    for i in range(len(bzobj.items)):
        if bzobj.nameCleaner(item_name) == bzobj.items[i]:
            itemindex = i
            break
    if itemindex == 0:
        return False
    if not bzobj.items2[itemindex].value() == -1 and not bzobj.items2[itemindex].price() == -1:
        return round(bzobj.items2[itemindex].value() - bzobj.items2[itemindex].price(), 2)
    else:
        return None

def specificitemprice(item_name):
    '''
    returns the price of a specific item
    :param item_name: (str)
    :return: (float)
    '''
    bzobj.updatePrices()
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
    bzobj.updatePrices()
    item_name = item_name.split()
    templist = []
    for x in item_name:
        x = x.capitalize()
        templist.append(x)
    item_name = " ".join(templist)
    return bzobj.items2[bzobj.items.index(item_name)].value()

def goldenTooth(MONEY):
    '''
    returns the amount of wolf teeth and enchanted gold to buy, along with the profit and amount of golden teeth it wil produce
    :param MONEY: (int)
    :return: (tuple)
    '''
    bzobj.updatePrices()
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
    pass