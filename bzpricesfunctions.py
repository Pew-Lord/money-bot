import bazaarpricesobj as bzobj

def itemnames():
    '''
    returns the api-specific name of every item
    :return: (list)
    '''
    return bzobj.items
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