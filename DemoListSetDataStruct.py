

myOriginalList = [1,2,3,3,2,4,5]
mySet = set(myOriginalList)
uniqueList1 = list(mySet)

print(myOriginalList)
print(uniqueList1)

uniqueList2 = []
for number in myOriginalList:
    if not number in uniqueList2:
        uniqueList2.append(number)

print(uniqueList2)

