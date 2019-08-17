class MathHelper:
    
    @staticmethod
    def isInt(value):
        try:
            value = int(value)
            return True

        except ValueError:
            return False

    @staticmethod
    def isValueEven(value):
        return True if (value % 2) == 0 else False