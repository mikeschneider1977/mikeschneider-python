myList = [1,2,3,4]
myList2 = ['a', 'b', 'c', 'd']
myList3 = [myList, myList]

print(myList + [5])


print(myList3)

print(myList3[0][1])

print(myList)

print(myList[0])

myList.insert(0,-1)

print(myList)

myList.insert(3, 100)

print(myList)

myList.insert(3, int(input("enter a number - ")))

print(myList)
print(myList2)
print(myList2[3])

print()

for letter in 'mike':
    print(letter)

print()

newList = [];
for i in range(0,2):
    print(i)
    newList.insert(i , input("enter a letter - "))

print(newList)

print(int(15/2))

print(15/2.0)

