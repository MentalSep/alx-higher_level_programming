#!/usr/bin/python3
""" Unittest for max_integer([..]) """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class for unittests """

    def test_empty_list(self):
        """ Test for empty list """
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """ Test for single element list"""
        self.assertEqual(max_integer([1]), 1)

    def test_sorted_list(self):
        """ Test for sorted list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_unsorted_list(self):
        """ Test for unsorted list"""
        self.assertEqual(max_integer([5, 3, 1, 4, 2]), 5)

    def test_negative_numbers(self):
        """ Test for negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        """ Test for mixed numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4, 0]), 4)

    def test_float_numbers(self):
        """ Test for float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5, 5.5]), 5.5)
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5, -5.5]), 4.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5, -4.5, -5.5]), -1.5)

    def test_string(self):
        """ Test for string"""
        self.assertEqual(max_integer("string"), 't')

    def test_tuple(self):
        """ Test for tuple"""
        self.assertEqual(max_integer((1, 2, 3, 4, 5)), 5)

    def test_list_of_strings(self):
        """ Test for list of strings"""
        self.assertEqual(max_integer(["a", "b", "c", "d", "e"]), 'e')

    def test_list_of_tuples(self):
        """ Test for list of tuples"""
        self.assertEqual(max_integer([(1, 2), (3, 4), (5, 6)]), (5, 6))

    def test_list_of_lists(self):
        """ Test for list of lists"""
        self.assertEqual(max_integer([[1, 2], [3, 4], [5, 6]]), [5, 6])

    def test_list_of_mixed_types(self):
        """ Test for list of mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 4, "string"])

    def test_None(self):
        """ Test for None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dictionary(self):
        """ Test for dictionary"""
        with self.assertRaises(KeyError):
            max_integer({1: "one", 2: "two", 3: "three"})

    def test_set(self):
        """ Test for set"""
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4, 5})

    def test_inf(self):
        """ Test for inf"""
        self.assertEqual(max_integer([1, 2, float('inf')]), float('inf'))

    def test_nan(self):
        """ Test for nan"""
        self.assertEqual(max_integer([1, 2, float('nan')]), 2)

    def test_inf_nan(self):
        """ Test for inf and nan"""
        self.assertEqual(max_integer([1, 2, float('inf'), float('nan')]),
                         float('inf'))
