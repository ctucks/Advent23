#import os
#os.getcdw()
#os.chdir("C:\\Users\\Chris\\Documents\\_coding\\Python\\AOC23\\Advent23")
from modules.parser import parseData

red = 12
green = 13
blue = 14

#import example data, and parse.
ex1Input = parseData('d2p1ex.txt', 'string')
ex1Input = parseData('d2p1input.txt', 'string')

#split game value and cube data.
ex1Data = []
for item in ex1Input:
    gData = item.split(':')
    ex1Data.append(gData)

#get game value and create cube data list.
ex1Sorted = []
for item in ex1Data:
    ex1Game = int((item[0].split(' '))[-1])
    ex1Cubes = item[1].split(';')
    ex1Sorted.append([ex1Game, ex1Cubes])
    print(ex1Game, '==', ex1Cubes)

ex1Cubes = []
for item in ex1Sorted:
    cubeRow = []
    ex1Game = item[0]
    cubeRow.append(ex1Game)
    for cubes in item[1]:
        cubeSplit = cubes.split(',')
        cubeRow.append(cubeSplit)
    ex1Cubes.append(cubeRow)

sumGames = 0
gameNum = 0
for item in ex1Cubes:
    gameNum += 1
    print(gameNum)
    #red = 12
    #green = 13
    #blue = 14
    ex1GameVal = item[0]
    for items in item[1:]:
        enoughCubes = True
        red = 12
        green = 13
        blue = 14
        for cubes in items:
            cubes = cubes.strip(' ')
            cubes = cubes.split(' ')
            #red
            if cubes[1] == 'red':
                red -= int(cubes[0])
            #green
            elif cubes[1] == 'green':
                green -= int(cubes[0])
            #blue
            elif cubes[1] == 'blue':
                blue -= int(cubes[0])
        if red >= 0 and green >= 0 and blue >= 0:
            print('ENOUGH CUBES', red, green, blue)
            #sumGames += int(ex1GameVal)
        else:
            enoughCubes = False
            print('NOT ENOUGH CUBES :(', red, green, blue)
            break
    if enoughCubes == True:
        print('enough cubes for full game', red, green, blue)
        sumGames += int(ex1GameVal)

#############################
## PART 2 ##
#############################

gameNum = 0
multiSum = 0
for item in ex1Cubes:
    gameNum += 1
    print(gameNum)
    red = 0
    green = 0
    blue = 0
    ex1GameVal = item[0]
    for items in item[1:]:
        for cubes in items:
            cubes = cubes.strip(' ')
            cubes = cubes.split(' ')
            #red
            if cubes[1] == 'red':
                cubeVal = int(cubes[0])
                if cubeVal > red:
                    red = cubeVal
            #green
            elif cubes[1] == 'green':
                cubeVal = int(cubes[0])
                if cubeVal > green:
                    green = cubeVal
            #blue
            elif cubes[1] == 'blue':
                cubeVal = int(cubes[0])
                if cubeVal > blue:
                    blue = cubeVal
    cubesMulti = red * green * blue
    multiSum += cubesMulti









