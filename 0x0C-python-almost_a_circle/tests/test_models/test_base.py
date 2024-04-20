from models.base import Base
import unittest

class TestBase(unittest.TestCase):

    def test_base(self):

        b1 = Base()
        val = b1.id
        self.assertEqual(val, 1)

        b2 = Base(99)
        val2 = b2.id
        self.assertEqual(val2, 99)

        b3 = Base()
        val3 = b3.id
        self.assertEqual(val3, 2)
