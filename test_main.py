import unittest
import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main.find_maxvalue([-3,4,3,-2,2,5], 4), 8)

        self.assertEqual(main.find_maxvalue([4,3,-2,9,-4,2,7], 6), 15)

if __name__== '__main__':
    unittest.main()