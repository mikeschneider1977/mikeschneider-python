def oneDice():
    for i in range(0, 3):
        if i == 0 or i == 2:
            for j in range (0, 9):
                if j == 0 or j == 8:
                    print("*", end='')
                else:
                    print(' ', end ='')
        else:
            for k in range(0, 9):
                if k == 0 or k == 4 or k == 8:
                    print('*', end ='')
                else:
                    print(' ', end ='')

        print()

def twoDice():
    for i in range(0, 3):
        if i == 0 or i == 2:
            for j in range (0, 9):
                if j == 0 or j == 8:
                    print("*", end='')
                else:
                    print(' ', end ='')
        else:
            for k in range(0, 9):
                if k == 0 or k == 3 or k == 5 or k == 8:
                    print('*', end ='')
                else:
                    print(' ', end ='')

        print()


def threeDice():
    for i in range(0, 3):
        if i == 0:
            for j in range (0, 9):
                if j == 0 or j == 2 or j == 8:
                    print("*", end='')
                else:
                    print(' ', end ='')
        elif i == 1:
            for j in range (0, 9):
                if j == 0 or j == 4 or j == 8:
                    print('*', end ='')
                else:
                    print(' ', end ='')
        else:
            for j in range (0, 9):
                if j == 0 or j == 6 or j == 8:
                    print('*', end ='')
                else:
                    print(' ', end ='')
        print()

def fourDice():
    for i in range(0, 3):
        if i == 0:
            for j in range (0, 9):
                if j == 0 or j == 3 or j == 5 or j == 8:
                    print("*", end='')
                else:
                    print(' ', end ='')
        elif i == 2:
            for j in range (0, 9):
                if j == 0 or j == 3 or j == 5 or j == 8:
                    print('*', end ='')
                else:
                    print(' ', end ='')
        else:
            for j in range (0, 9):
                if j == 0 or j == 8:
                    print('*', end ='')
                else:
                    print(' ', end ='')
        print()

def fiveDice():
    for i in range(0, 3):
        if i == 0:
            for j in range (0, 9):
                if j == 0 or j == 3 or j == 5 or j == 8:
                    print("*", end='')
                else:
                    print(' ', end ='')
        elif i == 1:
            for j in range (0, 9):
                if j == 0 or j == 4 or j == 8:
                    print('*', end ='')
                else:
                    print(' ', end ='')
        else:
            for j in range (0, 9):
                if j == 0 or j == 3 or j == 5 or j == 8:
                    print("*", end='')
                else:
                    print(' ', end ='')
        print()

def sixDice():
    for i in range(0, 3):
        for j in range (0, 9):
            if j == 0 or j == 3 or j == 5 or j == 8:
                print("*", end='')
            else:
                print(' ', end ='')
        print()
def printDice(dieCount):
    print('count = ' + str(dieCount))
    for i in range(0,9):
        print("*", end='')
    print()

    if dieCount == 1:
        oneDice()
    elif dieCount == 2:
        twoDice()
    elif dieCount == 3:
        threeDice()
    elif dieCount == 4:
        fourDice()
    elif dieCount == 5:
        fiveDice()
    else:
        sixDice()

    for i in range(0,9):
        print("*", end='')
    print()
