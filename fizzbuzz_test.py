import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz.fizzbuzz(32), "32")
        self.assertEqual(fizzbuzz.fizzbuzz(3), "3 fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(5), "5 buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(15), "15 fizzbuzz")
        
        
    
if __name__ == '__main__':
    unittest.main()