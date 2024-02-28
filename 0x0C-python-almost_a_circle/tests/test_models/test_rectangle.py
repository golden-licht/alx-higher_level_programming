#!/usr/bin/python3

from models.rectangle import Rectangle
import io
import json
import os
import sys
import unittest


class TestRectangle(unittest.TestCase):
    def test_init_method(self):
        """Test the `init` method"""
        # width and height given
        rect1 = Rectangle(1, 2)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)
        # width, height and x given
        rect2 = Rectangle(1, 2, 3)
        self.assertEqual(rect2.width, 1)
        self.assertEqual(rect2.height, 2)
        self.assertEqual(rect2.x, 3)
        # width, height, x and y given
        rect3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect3.width, 1)
        self.assertEqual(rect3.height, 2)
        self.assertEqual(rect3.x, 3)
        self.assertEqual(rect3.y, 4)
        # width not integer given
        self.assertRaises(TypeError, Rectangle, "1", 2)
        # height not integer given
        self.assertRaises(TypeError, Rectangle, 1, "2")
        # x not integer given
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        # y not integer given
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        # width, height, x, y and id given
        rect8 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect8.width, 1)
        self.assertEqual(rect8.height, 2)
        self.assertEqual(rect8.x, 3)
        self.assertEqual(rect8.y, 4)
        self.assertEqual(rect8.id, 5)
        # negative width given
        self.assertRaises(ValueError, Rectangle, -1, 2)
        # negative height given
        self.assertRaises(ValueError, Rectangle, 1, -2)
        # width zero given
        self.assertRaises(ValueError, Rectangle, 0, 2)
        # height zero given
        self.assertRaises(ValueError, Rectangle, 1, 0)
        # negative x given
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        # negative y given
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_area(self):
        """Test the `area` method"""
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_str(self):
        """"Test the `str` method"""
        rect = Rectangle(1, 2, 3, 4, 5)
        expected = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(rect.__str__(), expected)

    def test_display(self):
        """Test the `display` method"""
        # without x and y
        rect = Rectangle(2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect.display()
        printed_output = captured_output.getvalue()
        expected_output = "##\n"\
                          "##\n"
        self.assertEqual(printed_output, expected_output)
        # without y
        rect = Rectangle(2, 2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect.display()
        printed_output = captured_output.getvalue()
        expected_output = "  ##\n"\
                          "  ##\n"
        self.assertEqual(printed_output, expected_output)
        # with x and y given
        rect = Rectangle(2, 2, 2, 1)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect.display()
        printed_output = captured_output.getvalue()
        expected_output = "\n"\
                          "  ##\n"\
                          "  ##\n"
        self.assertEqual(printed_output, expected_output)
        sys.stdout = sys.__stdout__
 
    def test_to_dictionary(self):
        """Test the `to_dictionary` method"""
        rect = Rectangle(1, 2, 3, 4, 5)
        expected = {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
        self.assertEqual(rect.to_dictionary(), expected)

    def test_update(self):
        """Test the `update` method"""
        # no argument given
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update()
        expected = {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
        self.assertEqual(rect.to_dictionary(), expected)
        # update the id
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10)
        expected = {"id": 10, "width": 1, "height": 2, "x": 3, "y": 4}
        self.assertEqual(rect.to_dictionary(), expected)
        # update id and width
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20)
        expected = {"id": 10, "width": 20, "height": 2, "x": 3, "y": 4}
        self.assertEqual(rect.to_dictionary(), expected)
        # update id, width and height
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30)
        expected = {"id": 10, "width": 20, "height": 30, "x": 3, "y": 4}
        self.assertEqual(rect.to_dictionary(), expected)
        # update id, width, height and x
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40)
        expected = {"id": 10, "width": 20, "height": 30, "x": 40, "y": 4}
        self.assertEqual(rect.to_dictionary(), expected)
        # update id, width, height, x and y
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50)
        expected = {"id": 10, "width": 20, "height": 30, "x": 40, "y": 50}
        self.assertEqual(rect.to_dictionary(), expected)
        # update id given as key: value argument
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=10)
        expected = {"id": 10, "width": 1, "height": 2, "x": 3, "y": 4}
        self.assertEqual(rect.to_dictionary(), expected)
        # update id and width given as key: value arg
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=10, width=20)
        expected = {"id": 10, "width": 20, "height": 2, "x": 3, "y": 4}
        self.assertEqual(rect.to_dictionary(), expected)
        # update id, width and height given as key: value arg
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=10, width=20, height=30)
        expected = {"id": 10, "width": 20, "height": 30, "x": 3, "y": 4}
        self.assertEqual(rect.to_dictionary(), expected)
        # update id, width, height and x given as key: value
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=10, width=20, height=30, x=40)
        expected = {"id": 10, "width": 20, "height": 30, "x": 40, "y": 4}
        self.assertEqual(rect.to_dictionary(), expected)
        self.assertEqual(rect.to_dictionary(), expected)
        # update id, width, height, x and y given as key: value
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=10, width=20, height=30, x=40, y=50)
        expected = {"id": 10, "width": 20, "height": 30, "x": 40, "y": 50}
        self.assertEqual(rect.to_dictionary(), expected)

    def test_create(self):
        """Test the method `create` defined in the `Base` class"""
        # create a rectangle obj with given id
        rect =  Rectangle.create(id=89)
        self.assertEqual(rect.id, 89)
        # create a rect obj with id and width
        rect =  Rectangle.create(id=89, width=1)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        # create a rect obj with id, width, and height
        rect =  Rectangle.create(id=89, width=1, height=2)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        # create a rect obj with id, width, height, and x
        rect =  Rectangle.create(id=89, width=1, height=2, x=3)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        # create a rect obj with id, width, height, x, and y
        rect =  Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_save_to_file(self):
        """Test the method `save_to_file defined` in the `Base` class"""
        # None given
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertListEqual(json.load(f), [])
        # empty list given
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertListEqual(json.load(f), [])
        # a list of rectangle object given
        rect = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as f:
            expected = [{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]
            self.assertListEqual(json.load(f), expected)

    def test_load_from_file(self):
        """Test the method `load_from_file` defined in the `Base` class"""
        # when Rectangle.json doesn't exist
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEquals(Rectangle.load_from_file(), [])
        # when Rectangle.json exists
        with open("Rectangle.json", "w") as f:
            f.write('[{"id": 1, "width": 2,  "height": 3, "x": 4, "y": 5}]')
        list_of_objs = Rectangle.load_from_file()
        rect = list_of_objs[0]
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)


if __name__ == "__main__":
    unittest.main()
