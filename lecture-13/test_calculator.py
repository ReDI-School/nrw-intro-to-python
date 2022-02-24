import unittest
from calculator import Calculator

def setUpModule():
    print('set up module')

def tearDownModule():
    print('tear down module')

class TestCalculator(unittest.TestCase):

    # Ahead of every test, create a new calculator instance
    def setUp(self):
        print('Creating a new calculator')
        self.calc = Calculator()

    # Write test methods for subtract, multiply, and divide
    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9, msg=None)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(9, 7), 2, msg=None)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 7), 14, msg=None) 

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2, msg=None)

    @unittest.expectedFailure  # <- division by zero should actually raise an error
    def test_divide_by_zero(self):
        self.calc.divide(4, 0)
