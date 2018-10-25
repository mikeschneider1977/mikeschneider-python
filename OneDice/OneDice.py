import random

def main():

    setOfDice=[0] * 7 # create a list to store 6 dice types
    for i in range(1,7):
        setOfDice[i] = defineDice(i)
        printDice(setOfDice[i])

    input('pause')

    play = 'y'
    game = 0
    # prime with y for yes and keep playing until n for no
    while play == 'y':
        game += 1
        for i in range(0, 10):
            print('_', end ='')  # print a line between  each new roll

        print()

        print('game - ' + str(game))

        dice = rollDice()  # call rolldice and store results in setOfDice list

        printDice(setOfDice[dice])

        play = input('play again - y or n - ')  # keep playing or stop

    print('you played ' + str(game) + ' times')

def defineDice(num):
    if num == 1:
        return[' ------- ','|       |','|   *   |','|       |',' ------- ']
    elif num == 2:
        return[' ------- ','|       |','|  * *  |','|       |',' ------- ']
    elif num == 3:
        return[' ------- ','| *     |','|   *   |','|     * |',' ------- ']
    elif num == 4:
        return[' ------- ','|  * *  |','|       |','|  * *  |',' ------- ']
    elif num == 5:
        return[' ------- ','|  * *  |','|   *   |','|  * *  |',' ------- ']
    else:
        return[' ------- ','|  * *  |','|  * *  |','|  * *  |',' ------- ']

def rollDice():  # generate a random number between 1 and 6 to represent random roll of dice
    diceNum = random.randint(1, 6)
    return diceNum

def printDice(diceList):  # print the applicable dice to the console
    for i in diceList:
        print(i)

main()
