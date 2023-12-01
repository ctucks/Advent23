##############################################
                ## PART 2 ##
##############################################

import modules.parser

eData = open('C:\\Users\\Chris\\Documents\\_Coding\\Python\\AOC23\\Advent23\\D1_QData.txt')
#eData = open('AOC23\\D1_ExampleData.txt')
eList = []
for item in eData:    
    eList.append(item.strip())

eStrings = ['one','two','three','four','five','six','seven','eight','nine']
noMatch = 0
totalSum = 0
curIndex = 0

for items in eList:   
    print(items)         
    eStrints1 = []
    tempStrint = []
    for string in eStrings:
        if string in items:
            strintVal = str(eStrings.index(string) + 1)
            print(strintVal)
            indexVal = items.index(string)
            tempItem = [strintVal, indexVal]
            tempStrint += [tempItem]
            if items.count(string) >= 2:
                indexVal = items.rindex(string)
                tempStrint += [[strintVal, indexVal]]
    for item in items:
        try:
            itemInt = int(item)
            #print(item)
            #print("Item as integer:", itemInt)
            indexVal = items.index(item)
            tempItem = [item, indexVal]
            if tempItem in tempStrint:
                indexVal = items.rindex(item)
                tempStrint += [[item, indexVal]]
            else:
                tempStrint += [tempItem]
        except:
            noMatch += 1
            #print(item, "cannot be converted to an integer.")
    if len(tempStrint) >= 2:
        for item in tempStrint:
            #print(item)
            if len(eStrints1) == 0:
                eStrints1.append(item)
            else:
                if item[1] > eStrints1[-1][1]:
                    eStrints1.append(item)
                elif item[1] < eStrints1[0][1]:
                    eStrints1.insert(0,item)
        eStrints1Sum = ''
        eStrints1Sum += eStrints1[0][0]
        eStrints1Sum += eStrints1[-1][0]
        print(eStrints1Sum)
        totalSum += int(eStrints1Sum)
    elif len(tempStrint) == 1:
        eStrints1 = tempStrint
        print(int(tempStrint[0][0]))
        totalSum += int(tempStrint[0][0])
    print(tempStrint)
    print(eStrints1)

#51479


############################################
# everythig beyond here is just test stuff #
############################################


eStrints = []
eStrings = ['one','two','three','four','five','six','seven','eight','nine']
for items in eList:
    tempStrint= ''
    for string in eStrings:
        if string in items:
            print(string)
            strintVal = str(eStrings.index(string) + 1)
            indexVal = items.index(string)
            tempStrint += strintVal, indexVal
    if len(tempStrint) >= 2:
        sortedStrints = tempStrint[0]+ tempStrint[-1]
        eStrints.append(sortedStrints)
    if len(tempStrint) == 1:
        eStrints.append(tempStrint)
    
eStrintSum = 0
for item in eStrints:
    eStrintSum += int(item)

print(eStrintSum)


eStrints1 = []
tempStrint = []
for string in eStrings:
    if string in eData[0]:
        #print(string)
        strintVal = str(eStrings.index(string) + 1)
        #print(strintVal)
        indexVal = eData[0].index(string)
        tempStrint += [[strintVal, indexVal]]
for items in eData[0]:
    try:
        itemInt = int(items)
        #print("Item as integer:", itemInt)
        indexVal = eData[0].index(items)
        tempStrint += [[items, indexVal]]
    except:
        print("Item cannot be converted to an integer.")
if len(tempStrint) >= 2:
    for item in tempStrint:
        print(item)
        if len(eStrints1) < 2:
            eStrints1.append(item)
        else:
            if item[1] > eStrints1[-1][1]:
                eStrints1.append(item)
            elif item[1] == 0:
                eStrints1.insert(0,item)


eStrints1Sum = ''
eStrints1Sum += eStrints1[0][0]
eStrints1Sum += eStrints1[-1][0]

#newList = []
#for items in eList:
#    #eStrints1 = []
#    #tempStrint = []
#    for string in eStrings:
#        if string in items:
#            print(items)
#            #print(string)
#            modItem = items.replace(string, str(eStrings.index(string) + 1))
#            items = modItem
#            #strintVal = str(eStrings.index(string) + 1)
#            #print(strintVal)
#            #indexVal = items.index(string)
#            #tempStrint += [[strintVal, indexVal]]
#            newList.append(items)
#            curIndex += 1