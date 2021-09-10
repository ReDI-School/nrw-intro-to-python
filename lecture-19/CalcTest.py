import unittest
from calculator import *

def setUpModule():
    print('set up module')

def tearDownModule():
    print('tear down module')

class TestCalculator(unittest.TestCase):

    # Create an instance of the calculator that can be used in all tests
    @classmethod
    def setUpClass(self):
        print('Set up class')
        self.calc = Calculator()

    @classmethod
    def tearDownClass(self):
        print('Tear down class')

    # Write test methods for subtract, multiply, and divide
    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9, msg=None)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(9, 7), 2, msg=None)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 7), 14, msg=None) 

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2, msg=None)           


if __name__ == '__main__':
    unittest.main()