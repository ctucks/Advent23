
#find integers.
def q1_findInts(parsedList):
    nonInt = 0
    foundInts = []
    for items in parsedList:
        tempInts = ''
        for item in items:
            try:
                itemInt = int(item)
                #print("Item as integer:", itemInt)
                tempInts += item
            except:
                nonInt += 1
                #print("Item cannot be converted to an integer.")
        if len(tempInts) > 0:
            sortedInts = tempInts[0] + tempInts[-1]
            foundInts.append(sortedInts)
    return foundInts

#sum integers.
def q1_sumInts(foundInts):
    intSum = 0
    for item in foundInts:
        intSum += int(item)
    return intSum