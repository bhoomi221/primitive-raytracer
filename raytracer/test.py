import unittest

from vector import Vector 

class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0);
        self.v2 = Vector(3.0, 6.0, 9.0);

    def testMagnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    def test_addition(self):
        sum = self.v1 + self.v2
        self.assertEqual(getattr(sum, "x"), 4.0)
    
    def test_mult(self):
        sum = self.v1 * 4
        self.assertEqual(getattr(sum, "x"), 4.0)



if __name__ == "__main__":
    unittest.main()
