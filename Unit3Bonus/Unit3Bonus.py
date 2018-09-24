def changeNumbers(myList, x):
    print(myList)
    myResults = [0] * 4

    myResults[0] = myList[0] * x
    myResults[1] = myList[1] * x
    myResults[2] = myList[2] * x
    myResults[3] = myList[3] * x

    return(myResults)


































results = changeNumbers([1,2,3,4], 2)
print(results)
print()
results = changeNumbers(results, 3)
print(results)
print()
results = changeNumbers(results, 10)
print(results)



