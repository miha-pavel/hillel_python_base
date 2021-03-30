import unittest
from calcul import Calculator


#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # print("setUpClass")
        cls.calculator = Calculator()
    # #Each test method starts with the keyword test
    # def setUp(self):
    #     pass
    #     print("setUp")

    # def tearDown(self):
    #     pass
    #     print("tearDown")

    # @classmethod
    # def tearDownClass(cls):
    #     print("tearDownClass")

    
    # def test_add(self):
    #     # print('test_add: ')
    #     self.assertEqual(self.calculator.add(4, 7), 11)

    # def test_subtract(self):
    #     # print('test_subtract: ')
    #     self.assertEqual(5, self.calculator.subtract(10, 5))

    # def test_multiply(self):
    #     # print('test_multiply: ')
    #     self.assertEqual(self.calculator.multiply(3, 7), 21)

    def test_divide(self):
        # print('test_divide: ')
        self.assertEqual(self.calculator.divide(10, 2), 5)

    def test_divide_on_zero(self):
        # print('test_divide_zero: ')
        self.assertEqual(self.calculator.divide(10, 0), 'infinity')
        self.assertRaises(ZeroDivisionError)

    def test_divide_zero(self):
        # print('test_divide_zero: ')
        self.assertEqual(self.calculator.divide(0, 10), 0)

