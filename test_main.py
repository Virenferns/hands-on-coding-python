import unittest
import main

class TestMain(unittest.TestCase):
    def test_main(self):
        result = main.find_MaxValue([-3,4,3,-2,2,5], 4)
        self.assertEqual(result, 8)