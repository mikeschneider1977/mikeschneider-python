myList1 = [10, 20, 30, 40]

print(myList1)

print(len(myList1))

myList2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

mySubList1 = myList2[0:2]

print(mySubList1)

mySubList2 = myList2[5:10]

print(mySubList2)

mySubList2.append(51)

print(mySubList2)

print(mySubList2 + [52])

print(mySubList2)

popList = mySubList2.pop()

print(popList)
