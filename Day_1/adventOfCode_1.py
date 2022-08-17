from ast import main
import aoc_functions_1 as func


def main():
    inputData = func.getInputData()
    inputList = func.listifyInputData(inputData)
    nomOfIncreases = func.getNomOfDepthIncreases(inputList)
    print(nomOfIncreases)
    
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()