import unittest
import main

class TestMain(unittest.TestCase):
    def test_main(self):
        result = main.find_maxvalue([-3,4,3,-2,2,5], 4)
        self.assertEqual(result, 8)

        result = main.find_maxvalue([4,3,-2,9,-4,2,7], 6)
        self.assertEqual(result, 15)

if __name__== '__main__':
    unittest.main()