import unittest
from NumberComparator import NumberComparator

class NumberComparatorTester(unittest.TestCase):
    #test cases for geater than
    def test_two_positive_number_for_greater_than(self):
        output = NumberComparator(2.1, 1)
        self.assertTrue(output)

    def test_two_negative_number_for_greater_than(self):
        output = NumberComparator(-2.1, -8)
        self.assertTrue(output)

    def test_two_mixed_numbers_for_greater_than(self):
        output = NumberComparator(7, -3)
        self.assertTrue(output)


     #test cases for less than
    def test_two_positive_number_for_less_than(self):
        output = NumberComparator(1, 2.1)
        self.assertTrue(output)

    def test_two_negative_number_for_less_than(self):
        output = NumberComparator(-8, -7)
        self.assertTrue(output)

    def test_two_mixed_numbers_for_less_than(self):
        output = NumberComparator(-7, 3)
        self.assertTrue(output)

         #test cases for equal to
    def test_two_positive_number_for_equal_to(self):
        output = NumberComparator(2.1, 2.1)
        self.assertTrue(output)

    def test_two_negative_number_for_equal_to(self):
        output = NumberComparator(-8, -7)
        self.assertTrue(output)

    def test_two_mixed_numbers_for_equal_to(self):
        output = NumberComparator(-7, 3)
        self.assertTrue(output)

    




unittest.main() 