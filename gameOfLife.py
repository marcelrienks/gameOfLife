import sys
from helpers.printHelper import PrintHelper
from helpers.gridHelper import GridHelper
from helpers.mathHelper import MathHelper
from handlers.gameHandler import GameHandler

# Main method
def main():
    # Generate seed grid
    grid = preload()

    # Run
    gameHandler = GameHandler(grid)
    gameHandler.run()

# Collect input, and preload seed grid    
def preload():
    PrintHelper.clearScreen()

    # Collect intput and validate
    gridInput = input("Please enter the size and seed of the grid, split by a colon.\nSize will be used as the length of the grid in both directions.\nSeed will the number of live cells to start with, placed in random locations.\n(i.e. size:seed).\n")
    size, seed = validateGridInput(gridInput)    

    # Print grid and get confirmation to run
    grid = GridHelper.generateSeedGrid(size, seed)
    PrintHelper.printGrid(grid)
    shouldRun = input("\nWould you like to run this seed?\ny or n\n")
    
    if shouldRun == 'y':
        return grid
    
    else:
        return preload()

# Validate input variables
def validateGridInput(gridInput):
    # Validate that there is a split character
    if ":" not in gridInput:
        raise Exception ('Invalid input format, must be size:seed (e.g. 10:15)')

    size = gridInput.split(':')[0]
    seed = gridInput.split(':')[1]

    # validate that both inputs are integers
    if not MathHelper.isInt(size) and not MathHelper.isInt(seed):
        raise Exception ('Invalid input type, both size and seed must be integers (e.g. 10:15)')

    size = int(size)
    seed = int(seed)

    # validate that seed is not larger than the squared size
    if seed > (size * size):
        raise Exception ('Invalid input seed, must be smaller than the square of the size (e.g. 10:15)')

    return size, seed

if __name__ == '__main__':
    try:
        main()

    except Exception as ex:
        print('Exception:', ex)