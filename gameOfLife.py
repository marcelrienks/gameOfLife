import sys
import time
from helpers.printHelper import PrintHelper
from helpers.dataSetHelper import DataSetHelper

def main():
    try:
        PrintHelper.clearScreen()

        numberOfLiveCells = int(input("Please enter the number of live cells (between 1 - 100) that will be randomly generated for the seed.\n"))
        if numberOfLiveCells < 0 or numberOfLiveCells > 100:
            raise Exception()

        DataSetHelper.generateRandomDataSet(numberOfLiveCells)
        
    except ValueError:
      print('Input is not valid. Number must be between 1 - 100')

    except Exception as ex:
      print('Exception:', ex)

if __name__ == '__main__':
  main()

# Test
# dataSet = [[0,0,1,0,1,0,0,1,0,0],[0,0,0,1,0,1,0,0,1,0],[0,0,1,0,0,0,0,1,0,0],[0,0,0,0,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,1,1,0],[0,0,0,1,0,0,0,0,0,1],[1,1,1,1,1,0,0,0,0,0],[0,1,0,0,1,0,0,0,1,0],[0,1,0,0,1,0,1,0,0,0]]
# PrintHelper.printDataSet(dataSet)
# time.sleep(3)
# dataSet = [[0,0,1,1,1,0,1,0,0,0],[0,0,0,0,0,1,0,0,1,0],[0,0,1,1,0,0,0,1,0,1],[1,1,1,0,1,1,1,0,1,0],[1,0,0,0,0,1,0,0,0,0],[0,1,1,0,0,0,0,1,0,0],[0,1,1,1,0,0,1,0,0,1],[1,0,0,1,0,0,0,0,0,0],[0,0,1,0,1,0,0,0,1,0],[0,1,1,1,0,0,0,0,0,0]]
# PrintHelper.printDataSet(dataSet)