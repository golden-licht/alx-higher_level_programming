#!/usr/bin/python3

from models.base import Base
import json
import unittest


class TestBase(unittest.TestCase):
    def test_init_given_id(self):
        """Test the `init` method, given id"""
        base_object1 = Base(id=10)
        self.assertEqual(base_object1.id, 10)
        base_object2 = Base(id=0)
        self.assertEqual(base_object2.id, 0)
        base_object3 = Base(id=4)
        self.assertEqual(base_object3.id, 4)

    def test_init_without_given_id(self):
        """Test the `init` method, without given id"""
        base_object1 = Base()
        self.assertEqual(base_object1.id, 1)
        base_object2 = Base()
        self.assertEqual(base_object2.id, 2)

    def test_to_json_string(self):
        """Test for the method `to_json_string`"""
        # None given
        self.assertEqual(Base.to_json_string(None), "[]")
        # empty list given
        self.assertEqual(Base.to_json_string([]), "[]")
        # a list containing a dictionary given
        list_dict = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        self.assertIsInstance(Base.to_json_string(list_dict), str)
        self.assertEqual(Base.to_json_string(list_dict), json.dumps(list_dict))

    def test_from_json_string(self):
        """Test for the method `from_json_string`"""
        # None given
        self.assertListEqual(Base.from_json_string(None), [])
        # empty JSON string given
        self.assertListEqual(Base.from_json_string("[]"), [])
        # a JSON string representation of a list given
        json_string = '[{"id": 22}]'
        self.assertIsInstance(Base.from_json_string(json_string), list)
        self.assertListEqual(Base.from_json_string(json_string), [{"id": 22}])


if __name__ == "__main__":
    unittest.main()
