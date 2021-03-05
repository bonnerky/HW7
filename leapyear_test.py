import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.leapyear(-1), "error")
        
        
    
if __name__ == '__main__':
    unittest.main()