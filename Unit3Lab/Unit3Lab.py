
def printIt():
    print('williston high school')
    print('my fav subject is python')
    grade = input('what grade are you in ? - ')
    num = int(grade) - 1
    print(str(num))


def printIt2(city, grade):
    print(city)
    print(grade)

def boxArea(length, width):
    return(length * width)

def boxPerimeter(length, width):
    x = int(length)
    y = int(width)
    return(str(x + x + y + y))


#printIt()

#myCity = input('what city are you from? - ')
#myGrade = input('what grade in school are you? - ')

#printIt2(myCity, int(myGrade))

myLength = input('length please - ')
myWidth = input('width please - ')

print(str(boxArea(int(myLength), int(myWidth))))

print(boxPerimeter(myLength, myWidth))
