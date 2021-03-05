import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz.fizzbuzz(32), "32")
    
if __name__ == '__main__':
    unittest.main()