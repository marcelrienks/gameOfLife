import time
from helpers.printHelper import PrintHelper
from helpers.gridHelper import GridHelper

class GameHandler():

    def __init__(self, grid):
        self.grid = grid
    
    # Run conways game of life
    def run(self):
        iteration = 0
        while True:
            # Skip the seed grid, else calculate next lifecycle
            if iteration > 0:
                newGrid = self.calculateNextLifeCycle(self.grid)
                if newGrid != None:
                    self.grid = newGrid

                else:
                    break

            # Print the new grid
            iteration += 1
            PrintHelper.printGridLifeCycle(self.grid, iteration)
            time.sleep(0.3)

        print('Complete!')
    
    # Calculate the next life cycle grid
    def calculateNextLifeCycle(self, currentGrid):
        change = False
        newGrid = GridHelper.generateEmptyGrid(len(currentGrid[0]), len(currentGrid))

        for rowCoordinate in range(len(currentGrid)):
            for columnCoordinate in range(len(currentGrid[rowCoordinate])):
                # Get all the neighbours for the current grid cell
                neighbourCoordinates = GridHelper.getCellNeighbourCoordinates(len(currentGrid[0]), len(currentGrid), rowCoordinate, columnCoordinate)

                # count number of live neighbours
                liveNeighbours = 0
                for neighbourCoordinate in neighbourCoordinates:
                    neighbourCell = currentGrid[neighbourCoordinate[0]][neighbourCoordinate[1]]
                    if neighbourCell == 1:
                        liveNeighbours += 1
                
                # calculate the current cells next cycle life
                live = 0
                if currentGrid[rowCoordinate][columnCoordinate] == 1:

                    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                    if liveNeighbours < 2:
                        live = 0

                    # Any live cell with two or three live neighbours lives on to the next generation.
                    elif liveNeighbours > 1 and liveNeighbours < 4:
                        live = 1

                    # Any live cell with more than three live neighbours dies, as if by overpopulation.
                    elif liveNeighbours > 3:
                        live = 0

                else:
                    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                    if liveNeighbours == 3:
                        live = 1

                if currentGrid[rowCoordinate][columnCoordinate] != live:
                    change = True

                # populate current cell position of next life cycle grid
                newGrid[rowCoordinate][columnCoordinate] = live

        # return newly generated grid
        return newGrid if change == True else None
