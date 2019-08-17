from helpers.printHelper import PrintHelper
from helpers.gridHelper import GridHelper

class GameHandler():

    def __init__(self, grid):
        self.grid = grid
    
    def run(self):
        iteration = 0
        while True:
            # Skip the seed grid, else calculate next lifecycle
            if iteration > 0:
                self.grid = self.calculateNextLifeCycle(self.grid)

            iteration += 1
            PrintHelper.printGridLifeCycle(self.grid, iteration)
    
    def calculateNextLifeCycle(self, grid):
        for row in grid:
            for cell in row:
                # Get all the cells neighbours
                neighbourCoordinates = GridHelper.getCellNeighbourCoordinates(cell)

        return grid