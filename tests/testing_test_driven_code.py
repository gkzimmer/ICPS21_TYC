#This is a file for testing our test-driven development code in python
#This is the set-up for the very first commit.
#We'll start simple, pretending that we want a program that will be able to calculate
#number averages

import unittest
import random
import numpy as np
from testing_code import test_driven_code

class TestAdd(unittest.TestCase):

    def test_find_avg(self):
        expected = 5
        result = test_driven_code.find_avg(0,0,0,10,10,10)
        self.assertEqual(expected,result)

    #Now, let's try and test something slightly more advanced.
    #We want to write code that will round to the nearest whole number, which
    #we will test here.
    def test_find_avg_whole(self):
        expected = 5
        result = test_driven_code.find_avg(1,0,0,10,10,10)
        self.assertEqual(expected,result)

    #Now, let's test another function, this time finding the range of values
    def test_range(self):
        expected = 100
        result = test_driven_code.find_range(0,10,20,30,40,100)
        self.assertEqual(expected,result)
