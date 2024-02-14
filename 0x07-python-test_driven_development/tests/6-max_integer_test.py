#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class containing unittests for max_integer function"""

    def test_positive_numbers(self):
        """Test list of positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """Test list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """"Test mix of positive and negative list of numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_empty_list(self):
        """"Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test a single element"""
        self.assertEqual(max_integer([100]), 100)

    def test_float_numbers(self):
        """Test floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.75, 3.0, 4.2]), 4.2)


if __name__ == '__main__':
    unittest.main()
