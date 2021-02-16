try:
    import unittest2 as unittest
except ImportError:
    import unittest
    
import mycalc

class TestClass(unittest.TestCase):

    def test_add(self):
        result = mycalc.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(mycalc.add(10, 1), 11)

    def test_subtract(self):
        result = mycalc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_divide(self):
        self.assertEqual(mycalc.divide(10, 2), 5)

        with self.assertRaises(ValueError):
            mycalc.divide(10, 0)
            
    def test_multiply(self):
        self.assertEqual(mycalc.multiply(12, -3), -36)

    print("2 + 9 = ",mycalc.add(2,9))
    print("17 - 5 = ",mycalc.subtract(17,5))
    print("75 / 6 = ",mycalc.divide(75,6))
    print("13 * 2.3 = ",mycalc.multiply(13,2.3))

if __name__ == "__main__":
    unittest.main()

    

