import random
ROLLNUM = 2

def main():


    setOfDice=[0] * 6 # create a list to store 6 different dice
    for i in range(0,6):
        setOfDice[i] = defineDice(i)

    printDiceSideBySide(setOfDice) # print all six dice

    play = 'y'
    game = 0

    # prime with y for yes and keep playing until n for no
    while play == 'y':

        for i in range(0, 22):
            print('_', end ='')  # print a line between  each new roll

        print()
        game += 1
        print(' game - ' + str(game))


        myDice=[0] * ROLLNUM # list to store 2 dice
        roll = 0

        for i in range(0,ROLLNUM):
            roll = rollDice()
            print(str(roll + 1) + ' rolled', end = '\t')

            myDice[i] = setOfDice[roll]  # put the applicable roll of dice into list

        print()
        printDiceSideBySide(myDice)  # prints the dice you have rolled side by side

        play = input('play again - y or n - ')  # keep playing or stop

    print('you played ' + str(game) + ' times')

# defines 6 difrerent dice counts and returns the characters
# needed to print the dice to the console
def defineDice(num):
    topBot = ' ------- '
    blank = '|       |'
    oneDotL = '| *     |'
    oneDotM = '|   *   |'
    oneDotR = '|     * |'
    twoDot = '|  * *  |'
    if num == 0:
        return[topBot,blank,oneDotM, blank,topBot]
    elif num == 1:
        return[topBot,blank,twoDot,blank,topBot]
    elif num == 2:
        return[topBot,oneDotL,oneDotM,oneDotR,topBot]
    elif num == 3:
        return[topBot,twoDot,blank,twoDot,topBot]
    elif num == 4:
        return[topBot,twoDot,oneDotM,twoDot,topBot]
    else:
        return[topBot,twoDot,twoDot,twoDot,topBot]

def rollDice():  # generate a random number between 1 and 6 to represent random roll of dice
    diceNum = random.randint(0, 5)
    return diceNum

def printDice(diceList):  # print the applicable dice to the console one underneath the other
    for i in diceList:
        print(i)

# receives a list of the dice
def printDiceSideBySide(diceSet):
    for row in range(0, len(diceSet[0])):         # rows needed to display the dice (5)
        for col in range(0 , len(diceSet)):       # cols needed to display the dice
            print(diceSet[col][row], end = '\t')  # one col per dice
        print()

main()
