
#parse file as strings or lists
def parseData(fileName, splitType='string'):
    parseFile = open(fileName)
    parsedList = []
    if splitType == 'string':
        for item in parseFile:   
            parsedList.append(item.strip())
    elif splitType == 'list':
        for item in parseFile:
            parsedList.append(item.splitlines())
    else:
        print("""Please enter a valid splitType ('string' or 'list')""")
    return parsedList