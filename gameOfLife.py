import sys
import time
from helpers.printHelper import PrintHelper
from helpers.gridHelper import GridHelper
from helpers.mathHelper import MathHelper

def main():
    PrintHelper.clearScreen()

    gridInput = int(input("Please enter the size of the grid, and the number of live cells to seed (i.e. size:seed) (note size must be an even number).\n"))
    size, seed = validateGridInput(gridInput)

    if gridSize < 0 or gridSize > 100:
        raise Exception()

    grid = GridHelper.generateRandomGridMethod2(gridSize)
    PrintHelper.printDataSet(grid)

def validateGridInput(gridInput):
    if ":" not in gridInput:
        raise Exception ('Invalid input, format must be size:seed (e.g. 100:7)')

    size = gridInput.split(':')[0]
    seed = gridInput.split(':')[1]

    if not MathHelper.isValueEven(size) or :
        raise Exception ('Invalid input, format must be size:seed (e.g. 100:7)')

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