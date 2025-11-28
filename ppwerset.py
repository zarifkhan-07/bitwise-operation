import math

def printPowerSet(set, SetSize):
    PowerSetSize = int(math.pow(2, SetSize))
    for outer in range(PowerSetSize):
        for inner in range(SetSize):
            if (outer & (1 << inner)) > 0:
                print(set[inner], end=" ")
        print()

size = int(input("Enter array size: "))
set = [int(input("Enter element: ")) for _ in range(size)]
printPowerSet(set, len(set))
