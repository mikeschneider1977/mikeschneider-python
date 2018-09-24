def main():

    print('______________________________________________\n')
    print('Bellarmine Student current grade point average')
    print('______________________________________________\n')

    yearInt = input('What grade are you in? - ')

    # pass a number to function which will return the letter grade
    yearStr = getYearInSchool(int(yearInt))

    if(int(yearInt) >= 9 and int(yearInt) <= 12):
        print('\nCongrats you are a ' + yearStr)
    else:
        print(yearStr)

    # allClasses list can be 4 to 6 numbers
    allClasses = [66.0, 88.5, 41.0, 10, 22.9, 65]
    numClasses = len(allClasses)

    # pass a list to funciton that calculates GPA
    yourGpa = getGpa(allClasses, numClasses)
    print('\nYour current GPA is - ' + str(yourGpa))

    # pass GPA to function that determines your letter grade
    letterGrade = str(getLetterGrade(yourGpa))

    print('\nYour current Letter Grade is a - ' + letterGrade)

    if letterGrade == 'A' or letterGrade == 'B' or letterGrade == 'C':
        print('\nCongratulations you are passing')
    else:
        print('\nYikes - you are failing')




# returns long year and handles invalid year
def getYearInSchool(year):
    if year == 9:
        strYear = 'Freshman'
    elif year == 10:
        strYear = 'Sophomore'
    elif year == 11:
        strYear =  'Junior'
    elif year == 12:
        strYear = 'Senior'
    else:
        strYear = 'you are not in high school'

    return strYear


# returns GPA
def getGpa(myClasses, myNum):
    if myNum == 6:
        totalScore = myClasses[0] + myClasses[1] + myClasses[2] + myClasses[3] + myClasses[4] + myClasses[5]
    if myNum == 5:
        totalScore = myClasses[0] + myClasses[1] + myClasses[2] + myClasses[3] + myClasses[5]
    if myNum == 4:
        totalScore = myClasses[0] + myClasses[1] + myClasses[2] + myClasses[3]

    return totalScore / myNum


# using GPA rertruns letter grade
def getLetterGrade(numGrade):
    if numGrade > 90:
        letterGrade = 'A'
    elif numGrade > 80:
        letterGrade ='B'
    elif numGrade > 70:
        letterGrade = 'C'
    elif numGrade > 60:
        letterGrade = 'D'
    else:
        letterGrade = 'F'

    return letterGrade

# all functions have been defined - call main
main()


