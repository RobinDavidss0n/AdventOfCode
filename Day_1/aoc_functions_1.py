from aoc_inputData_1 import depthInput 


def getInputData():
    return depthInput

def listifyInputData(inputData):

    depthList = []
    depth = ""

    for char in inputData:
        if char == "\n":
            depthList.append(int(depth))
            depth = ""
        else:
            depth += char

    return depthList

def getNomOfDepthIncreases(depthList):
    nomOfIncreases = -1
    previousDepth = 0

    for depth in depthList:
        if depth > previousDepth:
            nomOfIncreases += 1
        previousDepth = depth
        
    return nomOfIncreases