class Calculator():
    """Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number,number)
    """
    def __init__(self):
        self._last_result = None

    def add(self, firstOperand, secondOperand):
        """Adds two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - Any number
        """
        self._last_result = firstOperand + secondOperand
        return self._last_result

    def subtract(self, firstOperand, secondOperand): 
        """Subtracts two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - Any number
        """
        self._last_result = firstOperand - secondOperand
        return self._last_result

    def multiply(self, firstOperand, secondOperand):
        """Multiplies two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - Any number
        """
        self._last_result = firstOperand * secondOperand
        return self._last_result

    def divide(self, firstOperand, secondOperand):   
        """Divides two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - Any number
        """
        self._last_result = firstOperand / secondOperand
        return self._last_result

    @property
    def last_result(self):
        """Read access to last result
        """
        return self._last_result