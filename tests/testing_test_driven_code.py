#This is a file for testing our test-driven development code in python
#This is the set-up for the very first commit.
#We'll start simple, pretending that we want a program that will be able to calculate
#number averages

import unittest
from my_package import test_driven_code

class TestAdd(unittest.TestCase):

    def test_find_avg(self):
        expected = 5
        result = test_driven_code.avg(1,1,1,10,10,10)
        self.assertEqual(expected,result)
