import unittest
from src.numerical_methods.numerical_bases import binToDeci, deciToBin

class TestBinaryDecimalConversion(unittest.TestCase):
    def test_binToDeci(self):
        self.assertAlmostEqual(binToDeci("110"), 6.0)
        self.assertAlmostEqual(binToDeci("1010"), 10.0)
        self.assertAlmostEqual(binToDeci("0.1"), 0.5)
        self.assertAlmostEqual(binToDeci("1.101"), 1.625)
        self.assertAlmostEqual(binToDeci("110.101"), 6.625)
        self.assertAlmostEqual(binToDeci("1001"), 9.0)
        self.assertAlmostEqual(binToDeci("1001."), 9.0)

    def test_deciToBin(self):
        self.assertEqual(deciToBin("6"), "110")
        self.assertEqual(deciToBin("10"), "1010")
        self.assertTrue(deciToBin("0.5").startswith("0.1"))
        self.assertTrue(deciToBin("1.625").startswith("1.101"))
        self.assertTrue(deciToBin("6.625").startswith("110.101"))
        self.assertEqual(deciToBin("9"), "1001")
        self.assertEqual(deciToBin("9."), "1001")

    def test_edge_cases(self):
        self.assertAlmostEqual(binToDeci("0.0001"), 0.0625)
        self.assertAlmostEqual(binToDeci("0.11111111111111111111"), 0.9999990463256836)
        self.assertEqual(deciToBin("1024"), "10000000000")
        self.assertEqual(binToDeci("1111110011.011"), 1011.375)
        self.assertEqual(deciToBin("12345.6789"), "11000000111001.10101101110011000110001111110001010000010010000001011")

if __name__ == "__main__":
    unittest.main()

