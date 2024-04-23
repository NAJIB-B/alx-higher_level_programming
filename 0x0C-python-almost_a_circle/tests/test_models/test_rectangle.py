from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):

    def test_id(self):

        r1 = Rectangle(10, 4)
        val = r1.id
        self.assertEqual(val, 1)

        r2 = Rectangle(12, 18)
        val2 = r2.id
        self.assertEqual(val2, 2)

        r3 = Rectangle(1, 14, 0, 0, 99)
        val3 = r3.id
        self.assertEqual(val3, 99)
