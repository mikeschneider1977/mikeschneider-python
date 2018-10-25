def main():
    inputString = input("give me a string ")
    print(inputString)
    noVowels = deVowel(inputString)
    print (noVowels)

    myList = ['a','b','c']
    print(myList)
    myList.remove('a')
    print(myList)

    someNumbers = [2, 4, 6, 8 ]
    print(someNumbers)

    calcNumbers = mathStuff(someNumbers, 3)
    print(calcNumbers)
    doStuff(1,1)


def deVowel(myString):
    returnString = ''

    for i in myString:

        if (i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'y'):
            if (i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U' and i != 'Y'):
                returnString = returnString + i

    return returnString


def mathStuff(myList, num):
    myCalcs = []

    for x in myList:
        myCalcs.append(x * num)

    return myCalcs

def doStuff(x,y):
    z = x + y




main()
