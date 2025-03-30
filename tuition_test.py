import unittest
from tuition_calc import calculate_tuition

class TestTutitionCalc(unittest.TestCase):
    def test_zero_credits(self):
        self.assertEqual(calculate_tuition(0, True, False), 0)
        self.assertEqual(calculate_tuition(0, True, True), 0)
        self.assertEqual(calculate_tuition(0, False, False), 0)
        self.assertEqual(calculate_tuition(0, False, True), 0)
    
    def test_one_credit(self):
        self.assertEqual(calculate_tuition(1, True, False), 822)
        self.assertEqual(calculate_tuition(1, True, True), 940)
        self.assertEqual(calculate_tuition(1, False, False), 1911)
        self.assertEqual(calculate_tuition(1, False, True), 2029)
    
    def test_eight_credits(self):
        self.assertEqual(calculate_tuition(8, True, False), 3391)
        self.assertEqual(calculate_tuition(8, True, True), 4335)
        self.assertEqual(calculate_tuition(8, False, False), 12103)
        self.assertEqual(calculate_tuition(8, False, True), 13047)
    
    def test_nine_credits(self):
        self.assertEqual(calculate_tuition(9, True, False), 4280.5)
        self.assertEqual(calculate_tuition(9, True, True), 5342.5)
        self.assertEqual(calculate_tuition(9, False, False), 14081.5)
        self.assertEqual(calculate_tuition(9, False, True), 15143.5)
    
    def test_eleven_credits(self):
        self.assertEqual(calculate_tuition(11, True, False), 5014.5)
        self.assertEqual(calculate_tuition(11, True, True), 6312.5)
        self.assertEqual(calculate_tuition(11, False, False), 16993.5)
        self.assertEqual(calculate_tuition(11, False, True), 18291.5)
    
    def test_twelve_credits(self):
        self.assertEqual(calculate_tuition(12, True, False), 5389.5)
        self.assertEqual(calculate_tuition(12, True, True), 6817.5)
        self.assertEqual(calculate_tuition(12, False, False), 18445.5)
        self.assertEqual(calculate_tuition(12, False, True), 19873.5)
    
    def test_fifteen_credits(self):
        self.assertEqual(calculate_tuition(15, True, False), 5389.5)
        self.assertEqual(calculate_tuition(15, True, True), 6817.5)
        self.assertEqual(calculate_tuition(15, False, False), 18445.5)
        self.assertEqual(calculate_tuition(15, False, True), 19873.5)
    
    def test_negative_credits(self):
        with self.assertRaises(ValueError):
            calculate_tuition(-1, True, False)
            calculate_tuition(-1, False, True)

if __name__ == "__main__":
    unittest.main()