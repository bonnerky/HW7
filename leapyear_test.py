import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.leapyear(-1), "error")
        self.assertEqual(leapyear.leapyear(5), "Year is not a leap year")
        
    
if __name__ == '__main__':
    unittest.main()