import random
import math

class GridHelper:
    
    @staticmethod
    def generateRandomGrid(size, seed):
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