import unittest
from main import *

class MyTestCase(unittest.TestCase):

    def test_elem_sum(self):
        a, b = 2, 3
        output = elem_sum(a, b)
        self.assertEqual(output, 5)
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()
