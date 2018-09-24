userInput = input("What is your numerical grade?")

numGrade = int(userInput)

if numGrade >= 90:
    print("Yahoo you got an A!")
    print("You know your stuff")
elif numGrade >= 80:
    print("Pretty good you got a B!")
elif numGrade >= 70:
    print("Okay you got a C!")
else:
    print("You better study harder!")

userInput = input("What is your favorite color?")

if userInput == 'blue':
    print("the sky is blue")
elif userInput == 'green':
    print('the forest is green')
elif userInput == 'red':
    print("i love red")
elif userInput == 'yellow':
    print("yuck yellow")
else:
    print('i am dumb computer and only know 4 colors')
