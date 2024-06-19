from models.rectangle import Rectangle
import sys
from io import StringIO
import unittest

class TestRectangle(unittest.TestCase):

    def test__id(self):

        
        r1 = Rectangle(1, 14)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 14, 0, 0)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(1, 14, 0, 0, 99)
        val3 = r3.id
        self.assertEqual(val3, 99)

    def test_validator(self):

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r2 = Rectangle("1", 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 4)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 4, -3, 3)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 4, 3, -5)

    def test_area(self):

        r1 = Rectangle(5, 5)
        r2 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 25)
        self.assertEqual(r2.area(), 50)

    def test_display_1(self):

        """redirecting stdout to stringIO"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        r1 = Rectangle(3, 3)
        expected_string = "###\n###\n###\n"
        r1.display()

        printed_text = captured_output.getvalue()

        sys.std = sys.__stdout__

        self.assertEqual(printed_text, expected_string)


    def test_display_2(self):

        """redirecting stdout to stringIO"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        r1 = Rectangle(3, 3, 2, 2)
        expected_string = "\n\n  ###\n  ###\n  ###\n"
        r1.display()

        printed_text = captured_output.getvalue()

        sys.std = sys.__stdout__

        self.assertEqual(printed_text, expected_string)

    def test_str(self):

        """redirecting stdout to stringIO"""

        captured_output = StringIO()
        sys.stdout = captured_output
        
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)

        expected_string = "[Rectangle] (12) 2/1 - 4/6\n"

        printed_text = captured_output.getvalue()

        sys.std = sys.__stdout__

        self.assertEqual(printed_text, expected_string)

    def test_update(self):

        r1 = Rectangle(10, 10, 10, 10)

        r1.update(80)
        self.assertEqual(r1.id, 80)
        
        r1.update(80, 2)
        self.assertEqual(r1.width, 2)

        r1.update(80, 2, 4)
        self.assertEqual(r1.height, 4)

        r1.update(80, 2, 4, 7)
        self.assertEqual(r1.x, 7)

        r1.update(80, 2, 4, 7, 8)
        self.assertEqual(r1.y, 8)

        r1.update(id=89)
        self.assertEqual(r1.id, 89)

        r1.update(width=60)
        self.assertEqual(r1.width, 60)

        r1.update(height=70)
        self.assertEqual(r1.height, 70)

        r1.update(x=77)
        self.assertEqual(r1.x, 77)

        r1.update(y=88)
        self.assertEqual(r1.y, 88)


        
