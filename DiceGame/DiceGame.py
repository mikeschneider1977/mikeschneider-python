import random

def main():

    play = 'y'
    game = 0
    roll = 1
    # prime with y for yes and keep playing until n for no
    while play == 'y':
        game += 1
        for i in range(0, 20):
            print('_', end ='')  # print a line between  each new roll

        print()

        print('game - ' + str(game))
        print('roll - ' + str(roll))

        setOfDice=[0] * 7 # create a list to store 6 dice types
        for i in range(1,7):
            setOfDice[i] = defineDice(i)

        ##myDice=[0] * 5
        ##for i in range(0,5):
        ##myDice[i] = \
        dice = rollDice()  # call rolldice and store results in setOfDice list

        ##for i in range(0 ,5):
        print('dice ' + str(i + 1))
        ##printDice(setOfDice[myDice[i]])
        printDice(setOfDice[dice])

        play = input('play again - y or n - ')  # keep playing or stop

def defineDice(num):
    if num == 1:
        return['---------','|       |','|   *   |','|       |','---------']
    elif num == 2:
        return['*********','*       *','*  * *  *','*       *','*********']
    elif num == 3:
        return['*********','* *     *','*   *   *','*     * *','*********']
    elif num == 4:
        return['*********','*  * *  *','*       *','*  * *  *','*********']
    elif num == 5:
        return['*********','*  * *  *','*   *   *','*  * *  *','*********']
    else:
        return['*********','*  * *  *','*  * *  *','*  * *  *','*********']

def rollDice():
    diceNum = random.randint(1, 6)
    return diceNum

def printDice(diceList):
    for i in diceList:
        print(i)

main()
