from operator import index
import os
import sys
import  aoc_functions_1 as func1

with open (os.path.join(sys.path[0], "input_part2.txt"), "r") as file:
    depthInput = file.read().splitlines()

trioList = []
trio = 0

for i, depth in enumerate(depthInput):

    for i2 in range(0,3):
        try:
            trio += int(depthInput[i+i2])
        except IndexError:
            print("Not mod 3 input data")
            break
    trioList.append(trio)
    trio = 0

# print(trioList)

nomOfDepthIncreases = func1.getNomOfDepthIncreases(trioList)

print(nomOfDepthIncreases)
