def main():
    draw7()
    print()
    starsAndStripes()
    print()
    increaseTriangle()
    print()
    bonusOne()
    print()
    bonusTwo()
    print('* ', end ='')

    print('* ', end ='')



    print('\\')
    print('\#')



def draw7():
    for i in range(0, 7):
        myString = ''
        for j in range(0, 7):
            myString += '* '
        print(myString)

def starsAndStripes():
    for i in range(0, 3):
        starString= ''
        stripeString= ''
        for x in range(0, 7):
            starString += '* '
            stripeString += '- '
        print(starString)
        print(stripeString)

def increaseTriangle():
    for i in range(1, 8):
        triString = ''
        for j in range(0, i):
            triString += str(i)
        print(triString)

def bonusOne():
    for i in range(0, 7):
        bString = ''
        if i == 0 or i == 6:
            for j in range(0, 7):
                bString += '* '
        else:
            for j in range(0, 7):
                if j == 0 or j == 6:
                    bString += '* '
                else:
                    bString += '- '
        print(bString)

def bonusTwo():
    for i in range(1, 8):
        triString = ''
        for j in range(1, (i + 1)):
            triString += str(j)
        print(triString)

    for i in range(6, 0, -1):
        triString = ''
        for j in range(1, (i + 1)):
            triString += str(j)
        print(triString)


main()
