def main():
    shoppingCart = [['tooth paste', 'q-tips', 'milk'], ['milk', 'candy', 'apples'], ['paper', 'pencils', 'q-tips']]

    oneShoppingCart = allInOne(shoppingCart)

    print(oneShoppingCart)

    qTipNum = countQTips(shoppingCart)

    print(qTipNum)

    moreMilkCart = drinkMoreMilk(shoppingCart)

    print(moreMilkCart)

    giveAMoose = mooseCookie(shoppingCart)

    print(giveAMoose)

#-------------------------------------------------

def allInOne(myShoppingCart):
    print('allInOne')

    oneCart = []

    for list in myShoppingCart:
        for item in list:
            if item not in oneCart:
                oneCart.append(item)

    return oneCart

#--------------------------------------------------

def countQTips(myShoppingCart):
    print('countQTips')

    qTipCount = 0

    for list in myShoppingCart:
        for item in list:
            if item == 'q-tips':
                qTipCount += 1

    return qTipCount
#---------------------------------------------------

def drinkMoreMilk(myShoppingCart):
    print('drinkMoreMilk')

    for list in myShoppingCart:
        if 'milk' not in list:
            list.append('milk')

    return myShoppingCart

#---------------------------------------------------

def mooseCookie(myShoppingCart):
    print('mooseCookie')

    for list in range(0, len(myShoppingCart)):
        for item in range(0, len(myShoppingCart[list])):
            if myShoppingCart[list][item] == 'milk':
                myShoppingCart[list][item] = 'milk and cookies'

    return myShoppingCart

#----------------------------------------------------

main()
