from os import system, name

class PrintHelper:

    # Clear the console screen
    @staticmethod
    def clearScreen():
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    
    # convert the dataset to a grid, and print it on the console
    @staticmethod
    def printGrid(grid):
        PrintHelper.clearScreen()
        for row in grid:
            printRow = ''
            for element in row:
                printRow += '□ ' if element == 0 else '■ '
                printRow.strip()
            print(printRow)