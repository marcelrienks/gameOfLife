import random
import math

class GridHelper:
    
    @staticmethod
    def generateSeedGrid(size, seed):
        #TODO convert this logic to use the cell model, which will container it's coordinates as well as it's value

        # Create empty grid
        grid = []
        for _ in range(size):
            grid.append([0] * size)

        # seed the grid
        for _ in range(seed):
            while True:
                row = random.randint(0,size - 1)
                cell = random.randint(0,size - 1)
                if grid[row][cell] == 0:
                    grid[row][cell] = 1
                    break

        return grid
    
    @staticmethod
    def getCellNeighbourCoordinates(cell):
        #TODO convert this logic to use the cell object, which will container it's coordinates as well as it's value

        coordinates = []
        
        coordinateSwitcher = CoordinateSwitcher(rowCoordinate, cellCoordinate)
        for index in range(1,9):
            coordinates.append(coordinateSwitcher.calculateNeighbourCoordinate(index))
        
        return coordinates

# this is how you create a dynamic Switch case in Python
class CoordinateSwitcher():

    def __init__(self, rowCoordinate, cellCoordinate):
        self.rowCoordinate = rowCoordinate
        self.cellCoordinate = cellCoordinate

    def calculateNeighbourCoordinate(self, neighbourIndex):
        method_name = 'neighbour_' + str(neighbourIndex)
        
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid neighbour index")
        
        # Call the method as we return it
        return method()
 
    def neighbour_1(self):
        return [self.rowCoordinate - 1, self.cellCoordinate - 1]
 
    def neighbour_2(self):
        return [self.rowCoordinate - 1, self.cellCoordinate]

    def neighbour_3(self):
        return [self.rowCoordinate - 1, self.cellCoordinate + 1]

    def neighbour_4(self):
        return [self.rowCoordinate, self.cellCoordinate - 1]
 
    def neighbour_5(self):
        return None

    def neighbour_6(self):
        return [self.rowCoordinate, self.cellCoordinate + 1]
    
    def neighbour_7(self):
        return [self.rowCoordinate + 1, self.cellCoordinate - 1]

    def neighbour_8(self):
        return [self.rowCoordinate + 1, self.cellCoordinate]

    def neighbour_9(self):
        return [self.rowCoordinate + 1, self.cellCoordinate + 1]