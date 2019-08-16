import random

class DataSetHelper:

    @staticmethod
    def generateRandomDataSet(numberOfLiveCells):
        # generate empty data range
        dataRange = [0] * 100

        # seed data range
        for _ in range(numberOfLiveCells):
            while True:
                index = random.randint(1,101)
                if dataRange[index] == 0:
                    dataRange[index] = 1
                    break

        # convert data range to dataSet
        dataset = [dataRange[0:10]]
        for row in range(10,100,10):
            dataset += [dataRange[row:row + 10]]

        return dataset