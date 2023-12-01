import aoc23_modules
import d1_modules

eData = open('AOC23\\D1_QData.txt')
qData = open('AOC23\\D1_ExampleData.txt')
e2Data = ['3oner4two', 'nxdthreefourfive']

d1p1Data = aoc23_modules.parseData(eData, 'string')
parsedData = d1_modules.q1_findInts(d1p1Data)
parsedInts = d1_modules.q1_sumInts(parsedData)
print(parsedInts)


##################
## non function ##
##################

# single list - combined into function? [x]
eList = []
for item in eData:    
    eList.append(item.strip())

#list of lists - combined into function? [x]
eList = []
for item in eData:   
    eList.append(item.splitlines())

#find int, combine, and add to list - # single list - combined into function? [x]
eInts = []
for items in eList:
    tempInts = ''
    for item in items:
        try:
            itemInt = int(item)
            #print("Item as integer:", itemInt)
            tempInts += item
        except:
            print("Item cannot be converted to an integer.")
    if len(tempInts) >= 2:
        sortedInts = tempInts[0] + tempInts[-1]
        eInts.append(sortedInts)
    elif len(tempInts) == 1:
        eInts.append(tempInts)

#find sum of ints in list - combined into function? [x]
eSum = 0
for item in eInts:
    eSum += int(item)