#!/usr/bin/python3

from models.square import Square 
import json
import os
import unittest


class TestSquare(unittest.TestCase):
    def test_init_method(self):
        """Test the `init` method"""
        # size given
        sqr1 = Square(1)
        self.assertEqual(sqr1.size, 1)
        # size and x given
        sqr2 = Square(1, 2)
        self.assertEqual(sqr2.x, 2)
        # size, x, and y given
        sqr3 = Square(1, 2, 3)
        self.assertEqual(sqr3.y, 3)
        # size not integer given
        self.assertRaises(TypeError, Square, "1")
        # x not integer given
        self.assertRaises(TypeError, Square, "2")
        # y not integer given
        self.assertRaises(TypeError, Square, 2, "3")
        # size, x, y, and id given
        sqr4 = Square(1, 2, 3, 4)
        self.assertEqual(sqr4.id, 4)
        # negative size given
        self.assertRaises(ValueError, Square, -1)
        # negative x given
        self.assertRaises(ValueError, Square, -2)
        # negative y given
        self.assertRaises(ValueError, Square, 2, -3)
        # size 0 given
        self.assertRaises(ValueError, Square, 0)

    def test_str(self):
        """"Test the `str` method"""
        sqr = Square(1, 2, 3, 4)
        expected = "[Square] (4) 2/3 - 1"
        self.assertEqual(sqr.__str__(), expected)
    
    def test_update(self):
        """Test the `update` method"""
        # no argument given
        sqr = Square(2, 3, 4, 5)
        sqr.update()
        expected = {"id": 5, "size": 2, "x": 3, "y": 4}
        self.assertEqual(sqr.to_dictionary(), expected)
        # update the id
        sqr = Square(2, 3, 4, 5)
        sqr.update(10)
        expected = {"id": 10, "size": 2, "x": 3, "y": 4}
        self.assertEqual(sqr.to_dictionary(), expected)
        # update id, and size
        sqr = Square(2, 3, 4, 5)
        sqr.update(10, 30)
        expected = {"id": 10, "size": 30, "x": 3, "y": 4}
        self.assertEqual(sqr.to_dictionary(), expected)
        # update id, size and x
        sqr = Square(2, 3, 4, 5)
        sqr.update(10, 30, 40)
        expected = {"id": 10, "size": 30, "x": 40, "y": 4}
        self.assertEqual(sqr.to_dictionary(), expected)
        # update id, size, x and y
        sqr = Square(2, 3, 4, 5)
        sqr.update(10, 30, 40, 50)
        expected = {"id": 10, "size": 30, "x": 40, "y": 50}
        self.assertEqual(sqr.to_dictionary(), expected)
        # update id given as key: value argument
        sqr = Square(2, 3, 4, 5)
        sqr.update(id=10)
        expected = {"id": 10, "size": 2, "x": 3, "y": 4}
        self.assertEqual(sqr.to_dictionary(), expected)
        # update id and size given as key: value arg
        sqr = Square(2, 3, 4, 5)
        sqr.update(id=10, size=20)
        expected = {"id": 10, "size": 20, "x": 3, "y": 4}
        self.assertEqual(sqr.to_dictionary(), expected)
        # update id, size and x given as key: value
        sqr = Square(2, 3, 4, 5)
        sqr.update(id=10, size=30, x=40)
        expected = {"id": 10, "size": 30, "x": 40, "y": 4}
        self.assertEqual(sqr.to_dictionary(), expected)
        self.assertEqual(sqr.to_dictionary(), expected)
        # update id, size, x and y given as key: value
        sqr = Square(2, 3, 4, 5)
        sqr.update(id=10, size=30, x=40, y=50)
        expected = {"id": 10, "size": 30, "x": 40, "y": 50}
        self.assertEqual(sqr.to_dictionary(), expected)

    def test_create(self):
        """Test the method `create` defined in the `Base` class"""
        # create a Square obj with given id
        sqr =  Square.create(id=89)
        self.assertEqual(sqr.id, 89)
        # create a sqr obj with id, and size
        sqr =  Square.create(id=89, size=2)
        self.assertEqual(sqr.id, 89)
        self.assertEqual(sqr.size, 2)
        # create a sqr obj with id, size, and x
        sqr =  Square.create(id=89, size=2, x=3)
        self.assertEqual(sqr.id, 89)
        self.assertEqual(sqr.size, 2)
        self.assertEqual(sqr.x, 3)
        # create a sqr obj with id,size, x, and y
        sqr =  Square.create(id=89,  size=2, x=3, y=4)
        self.assertEqual(sqr.id, 89)
        self.assertEqual(sqr.size, 2)
        self.assertEqual(sqr.x, 3)
        self.assertEqual(sqr.y, 4)

    def test_save_to_file(self):
        """Test the method `save_to_file defined` in the `Base` class"""
        # None given
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertListEqual(json.load(f), [])
        # empty list given
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertListEqual(json.load(f), [])
        # a list of Square object given
        sqr = Square(2, 3, 4, 5)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as f:
            expected = [{"id": 5, "size": 2, "x": 3, "y": 4}]
            self.assertListEqual(json.load(f), expected)

    def test_load_from_file(self):
        """Test the method `load_from_file` defined in the `Base` class"""
        # when Square.json doesn't exist
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEquals(Square.load_from_file(), [])
        # when Square.json exists
        with open("Square.json", "w") as f:
            f.write('[{"id": 1, "size": 3, "x": 4, "y": 5}]')
        list_of_objs = Square.load_from_file()
        sqr = list_of_objs[0]
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 3)
        self.assertEqual(sqr.x, 4)
        self.assertEqual(sqr.y, 5)


if __name__ == "__main__":
    unittest.main()
