import bazaarpricesobj as bzobj

def itemnames():
    '''
    returns the name of every item (putting the exact text written for an item will trigger
    commands (eg. $price ____))
    :return: (str) (str) (str) (str)
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
    :return: (dict)
    '''
    itemprices = {}
    for i in range(len(bzobj.items)):
        if bzobj.items2[i].price() == -1:
            continue
        itemprices[bzobj.items[i]] = bzobj.items2[i].price()
    return itemprices
def itemvalues():
    '''
    returns the name and value of every item
    :return: (dict)
    '''
    itemprices = {}
    for i in range(len(bzobj.items)):
        if bzobj.items2[i].value() == -1:
            continue
        itemprices[bzobj.items[i]] = bzobj.items2[i].value()
    return itemprices
def specificitemprice(item_name):
    '''
    returns the price of a specific item
    :param item_name: (str)
    :return: (float)
    '''
    return bzobj.items2[bzobj.items.index(item_name)].price()
def specificitemvalue(item_name):
    '''
    returns the value of a specific item
    :param item_name: (str)
    :return: (float)
    '''
    return bzobj.items2[bzobj.items.index(item_name)].value()