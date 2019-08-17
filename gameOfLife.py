import sys
import time
from helpers.printHelper import PrintHelper
from helpers.gridHelper import GridHelper
from helpers.mathHelper import MathHelper

def main():
    PrintHelper.clearScreen()

    gridInput = input("Please enter the size of the grid, and the number of live cells to seed (i.e. size:seed).\n")
    size, seed = validateGridInput(gridInput)

    grid = GridHelper.generateRandomGridMethod2(size, seed)
    PrintHelper.printDataSet(grid)

def validateGridInput(gridInput):
    if ":" not in gridInput:
        raise Exception ('Invalid input format, must be size:seed (e.g. 100:7)')

    size = gridInput.split(':')[0]
    seed = gridInput.split(':')[1]

    if not MathHelper.isInt(size) and not MathHelper.isInt(seed):
        raise Exception ('Invalid input type, both size and seed must be integers (e.g. 100:7)')

    size = int(size)
    seed = int(seed)

    if seed > size:
        raise Exception ('Invalid input seed, must be smaller than size (e.g. 100:7)')

    if not MathHelper.isValueEven(size):
        raise Exception ('Invalid input size, must be an even number (e.g. 100:7)')

    return size, seed

if __name__ == '__main__':
    try:
        main()

    except Exception as ex:
        print('Exception:', ex)

# Test
# dataSet = [[0,0,1,0,1,0,0,1,0,0],[0,0,0,1,0,1,0,0,1,0],[0,0,1,0,0,0,0,1,0,0],[0,0,0,0,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,1,1,0],[0,0,0,1,0,0,0,0,0,1],[1,1,1,1,1,0,0,0,0,0],[0,1,0,0,1,0,0,0,1,0],[0,1,0,0,1,0,1,0,0,0]]
# PrintHelper.printDataSet(dataSet)
# time.sleep(3)
# dataSet = [[0,0,1,1,1,0,1,0,0,0],[0,0,0,0,0,1,0,0,1,0],[0,0,1,1,0,0,0,1,0,1],[1,1,1,0,1,1,1,0,1,0],[1,0,0,0,0,1,0,0,0,0],[0,1,1,0,0,0,0,1,0,0],[0,1,1,1,0,0,1,0,0,1],[1,0,0,1,0,0,0,0,0,0],[0,0,1,0,1,0,0,0,1,0],[0,1,1,1,0,0,0,0,0,0]]
# PrintHelper.printDataSet(dataSet)