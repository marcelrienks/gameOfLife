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
    def printDataSet(dataSet):
        PrintHelper.clearScreen()
        for dataRow in dataSet:
            printRow = ''
            for dataElement in dataRow:
                printRow += '□ ' if dataElement == 0 else '■ '
                printRow.strip()
            print(printRow)