numList = [10,20,30,40,50,60,70,80,90,100]

print(numList)

print(len(numList))

print(numList[0])

print(numList[len(numList)-1])

subList = numList[0:5]

print(subList)

subList.insert(2,55)

print(subList)

subList.append(60)

print(subList)

subList1 = subList + [65]

print(subList1)

myClasses = ['math', 'english', 'history', 'python']

print(myClasses)

myClasses.remove('english')

print(myClasses)

favClass = myClasses.pop()

print('my fav class is ' + favClass)

