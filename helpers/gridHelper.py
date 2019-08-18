import random
import math

class GridHelper:
    
    # Create empty grid
    @staticmethod
    def generateEmptyGrid(size):
        grid = []
        for _ in range(size):
            grid.append([0] * size)
        
        return grid

    # Create a seeded grid
    @staticmethod
    def generateSeedGrid(size, seed):
        grid = GridHelper.generateEmptyGrid(size)

        # seed the grid
        for _ in range(seed):
            while True:
                row = random.randint(0, size - 1)
                column = random.randint(0, size - 1)
                if grid[row][column] == 0:
                    grid[row][column] = 1
                    break

        return grid
    
    # Get coordinate list of all the cells neighbours
    @staticmethod
    def getCellNeighbourCoordinates(gridSize, rowCoordinate, columnCoordinate):
        neighbourCoordinates = []
        
        # create a coordinate switcher and loop through all 8 possible neighbours to calculate their coordinate, using the current cell coordinates as the origin
        coordinateSwitcher = CoordinateSwitcher(gridSize, rowCoordinate, columnCoordinate)
        for index in range(1,10):
            coordinates = coordinateSwitcher.calculateNeighbourCoordinate(index)
            if coordinates != None:
                neighbourCoordinates.append(coordinates)
        
        return neighbourCoordinates

# this is how you create a dynamic Switch case in Python
class CoordinateSwitcher():

    def __init__(self, gridSize, rowCoordinate, columnCoordinate):
        self.gridSize = gridSize
        self.rowCoordinate = rowCoordinate
        self.columnCoordinate = columnCoordinate

    # calculate the coordinates of a neighbour of current cell coordinates
    def calculateNeighbourCoordinate(self, neighbourIndex):
        method_name = 'neighbour_' + str(neighbourIndex)
        
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid neighbour index")
        
        # Call the method as we return it
        return method()
 
    # calculate the top left neighbour coordinates, checking for whether current cell is not on the edge
    def neighbour_1(self):
        if self.rowCoordinate > 0 and self.columnCoordinate > 0:
            return [self.rowCoordinate - 1, self.columnCoordinate - 1]

        else:
            return None
 
    # calculate the top middle neighbour coordinates, checking for whether current cell is not on the edge
    def neighbour_2(self):
        if self.rowCoordinate > 0:
            return [self.rowCoordinate - 1, self.columnCoordinate]
        
        else:
            return None

    # calculate the top right neighbour coordinates, checking for whether current cell is not on the edge
    def neighbour_3(self):
        if self.rowCoordinate > 0 and self.columnCoordinate < (self.gridSize - 1):
            return [self.rowCoordinate - 1, self.columnCoordinate + 1]
        
        else:
            return None

    # calculate the left neighbour coordinates, checking for whether current cell is not on the edge
    def neighbour_4(self):
        if self.columnCoordinate > 0:
            return [self.rowCoordinate, self.columnCoordinate - 1]
 
        else:
            return None

    # ignore the current cell
    def neighbour_5(self):
        return None

    # calculate the top right neighbour coordinates, checking for whether current cell is not on the edge
    def neighbour_6(self):
        if self.columnCoordinate < (self.gridSize - 1):
            return [self.rowCoordinate, self.columnCoordinate + 1]
            
        else:
            return None
    
    # calculate the bottom left neighbour coordinates, checking for whether current cell is not on the edge
    def neighbour_7(self):
        if self.rowCoordinate < (self.gridSize - 1) and self.columnCoordinate > 0:
            return [self.rowCoordinate + 1, self.columnCoordinate - 1]
            
        else:
            return None

    # calculate the bottom middle neighbour coordinates, checking for whether current cell is not on the edge
    def neighbour_8(self):
        if self.rowCoordinate < (self.gridSize - 1):
            return [self.rowCoordinate + 1, self.columnCoordinate]
        
        else:
            return None

    # calculate the bottom right neighbour coordinates, checking for whether current cell is not on the edge
    def neighbour_9(self):
        if self.rowCoordinate < (self.gridSize - 1) and self.columnCoordinate < (self.gridSize - 1):
            return [self.rowCoordinate + 1, self.columnCoordinate + 1]
            
        else:
            return None