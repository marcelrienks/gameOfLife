import random

class GridHelper:

    @staticmethod
    def generateRandomGridMethod1(numberOfLiveCells):
        # generate empty data range
        dataRange = [0] * 100

        # seed data range
        for _ in range(numberOfLiveCells):
            while True:
                index = random.randint(0,99)
                if dataRange[index] == 0:
                    dataRange[index] = 1
                    break

        # convert data range to grid
        grid = [dataRange[0:10]]
        for row in range(10,100,10):
            grid += [dataRange[row:row + 10]]

        return grid
    
    @staticmethod
    def generateRandomGridMethod2(numberOfLiveCells):
        # Create empty grid
        grid = []
        for _ in range(10):
            grid.append([0] * 10)

        # seed the grid
        for _ in range(numberOfLiveCells):
            while True:
                row = random.randint(0,9)
                cell = random.randint(0,9)
                if grid[row][cell] == 0:
                    grid[row][cell] = 1
                    break

        return grid