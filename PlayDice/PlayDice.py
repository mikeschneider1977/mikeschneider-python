import random
ROLLNUM = 2

def main():


    setOfDice=[0] * 6 # create a list to store 6 different dice
    for i in range(0,6):
        setOfDice[i] = defineDice(i)

    #printDiceSideBySide(setOfDice) # print all six dice

    play = 'y'
    game = 0

    # prime with y for yes and keep playing until n for no
    while play == 'y':

        game += 1  # keep track of game count

        dice1 = int(input(' dice 1 - '))  # first dice to track
        dice2 = int(input(' dice 2 - '))  # second dice to track

        for i in range(0, 22):
            print('_', end ='')  # print a line between  each new roll

        print()

        print(' game - ' + str(game))  # prints game number

        bam = 'n'

        diceNumber = [0] * ROLLNUM  # variable to store the dice numbers rolled
        rolls = 0

        while bam == 'n':  #  play until both numbers input are rolled

            myDice=[0] * ROLLNUM # list to store 2 dice
            roll = 0
            rolls += 1     # counter to keep track of how many rolls needed to roll the two numbers input
            print(str(dice1) + ' needed\t' + str(dice2) + ' needed')

            for i in range(0,ROLLNUM):  # roll each dice to number of dice used
                roll = rollDice()
                print(str(roll + 1) + ' rolled', end = '\t')
                diceNumber[i] = roll + 1
                myDice[i] = setOfDice[roll]  # put the applicable roll of dice into list

            print()
            printDiceSideBySide(myDice)  # prints the dice you have rolled side by side

            # check to see if numbers entered have been rolled
            if diceNumber[0] == dice1 and diceNumber[1] == dice2:
                print('it took ' + str(rolls) + ' rolls')
                bam = 'y'
            elif diceNumber[0] == dice2 and diceNumber[1] == dice1:
                print('it took ' + str(rolls) + ' rolls')
                bam = 'y'
            else:
                bam = 'n'



        play = input('play again - y or n - ')  # keep playing or stop

    print('you played ' + str(game) + ' times')

# defines 6 different dice counts and returns the characters
# needed to print the dice to the console
def defineDice(num):
    topBot = ' ------- '
    blank = '|       |'
    oneDotL = '| *     |'
    oneDotM = '|   *   |'
    oneDotR = '|     * |'
    twoDot = '|  * *  |'
    if num == 0:   # dice with one dot
        return[topBot,blank,oneDotM, blank,topBot]
    elif num == 1: # dice with two dots
        return[topBot,blank,twoDot,blank,topBot]
    elif num == 2: # dice with three dots
        return[topBot,oneDotL,oneDotM,oneDotR,topBot]
    elif num == 3: # dice with four dots
        return[topBot,twoDot,blank,twoDot,topBot]
    elif num == 4: # dice with five dots
        return[topBot,twoDot,oneDotM,twoDot,topBot]
    else:          # dice with six dots
        return[topBot,twoDot,twoDot,twoDot,topBot]

def rollDice():  # generate a random number between 1 and 6 to represent random roll of dice
    diceNum = random.randint(0, 5)
    return diceNum

# receives a list of the dice
def printDiceSideBySide(diceSet):
    for row in range(0, len(diceSet[0])):         # rows needed to display the dice (5)
        for col in range(0 , len(diceSet)):       # cols needed to display the dice
            print(diceSet[col][row], end = '\t')  # one col per dice
        print()

main()
