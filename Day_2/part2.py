import os
import sys
with open (os.path.join(sys.path[0], "input.txt"), "r") as file:
    input = file.read().splitlines()

x = 0
y = 0
aim = 0

for line in input:
    value = int(line.split(" ")[1])

    #print(value)

    if "down" in line:
        aim += value

    if "up" in line:
        aim -= value

    if "forward" in line:
        x += value
        y += (aim*value)



print (x*y)
    
