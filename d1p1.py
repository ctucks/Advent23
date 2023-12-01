##############################################
                ## PART 2 ##
##############################################

import modules.parser
import d1modules.d1mod

qData = open('AOC23\\D1_ExampleData.txt')
e2Data = ['3oner4two', 'nxdthreefourfive']

eData = 'C:\\Users\\Chris\\Documents\\_Coding\\Python\\AOC23\\Advent23\\D1_QData.txt'
d1p1Data = modules.parser.parseData(eData, 'string')
parsedData = d1modules.d1mod.q1_findInts(d1p1Data)
parsedInts = d1modules.d1mod.q1_sumInts(parsedData)
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