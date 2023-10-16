#!/usr/bin/python3
""" unittest for modules in models directory """
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """ unittest for Base class """
    def test_docs(self):
        """ tests for module docstring """
        self.assertTrue(len(Base.__doc__) > 0)
        self.assertTrue(len(Base.__init__.__doc__) > 0)
        self.assertTrue(len(Base.to_json_string.__doc__) > 0)
        self.assertTrue(len(Base.save_to_file.__doc__) > 0)
        self.assertTrue(len(Base.from_json_string.__doc__) > 0)
        self.assertTrue(len(Base.create.__doc__) > 0)
        self.assertTrue(len(Base.load_from_file.__doc__) > 0)
        self.assertTrue(len(Base.save_to_file_csv.__doc__) > 0)
        self.assertTrue(len(Base.load_from_file_csv.__doc__) > 0)
        self.assertTrue(len(Base.draw.__doc__) > 0)

    def test_to_json_string(self):
        """ tests for to_json_string method """
        # test normal use
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        json_dict = Base.to_json_string([r1_dict])
        self.assertEqual(type(json_dict), str)
        self.assertEqual(json.loads(json_dict), [r1_dict])
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([r1_dict], 1)

    def test_save_to_file(self):
        """ tests for save_to_file method """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()),
                             [r1.to_dictionary(), r2.to_dictionary()])
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [])
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [])
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([r1, r2], 1)

    def test_from_json_string(self):
        """ tests for from_json_string method """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        json_dict = Base.to_json_string([r1_dict])
        self.assertEqual(type(json_dict), str)
        self.assertEqual(json.loads(json_dict), [r1_dict])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])
        with self.assertRaises(TypeError):
            Base.from_json_string()
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", 1)

    def test_create(self):
        """ tests for create method """
        self.assertIsNone(Base.create(**{'id': '89'}))
        self.assertIsNone(Base.create())
        self.assertIsNotNone(Rectangle.create())
        self.assertIsNotNone(Square.create())
        dictio = {"id": 89, "width": 3, "height": 4, "x": 2, "y": 1}
        a = Rectangle(3, 4, 2, 1, 89)
        b = Rectangle.create(**dictio)
        self.assertEqual(a.id, b.id)
        self.assertEqual(a.width, b.width)
        self.assertEqual(a.height, b.height)
        self.assertEqual(a.x, b.x)
        self.assertEqual(a.y, b.y)
        dictio = {"id": 89, "size": 5, "x": 2, "y": 1}
        a = Square(5, 2, 1, 89)
        b = Square.create(**dictio)
        self.assertEqual(a.id, b.id)
        self.assertEqual(a.width, b.width)
        self.assertEqual(a.height, b.height)
        self.assertEqual(a.x, b.x)
        self.assertEqual(a.y, b.y)

    def test_load_from_file(self):
        """ tests for load_from_file method """
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertEqual(list_rectangles_output[0].__str__(), "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rectangles_output[1].__str__(), "[Rectangle] (2) 0/0 - 2/4")
        Rectangle.save_to_file(None)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output), 0)
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(1)
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([r1, r2], 1)

    def test_save_to_file_csv(self):
        """ tests for save_to_file_csv method """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "[{\"id\": 1, \"width\": 10, \"height\": 7, \"x\": 2, \"y\": 8}, {\"id\": 2, \"width\": 2, \"height\": 4, \"x\": 0, \"y\": 0}]")
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "[]")
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "[]")
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([r1, r2], 1)

    def test_load_from_file_csv(self):
        """ tests for load_from_file_csv method """
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        self.assertEqual(Square.load_from_file_csv(), [])
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertEqual(list_rectangles_output[0].__str__(), "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rectangles_output[1].__str__(), "[Rectangle] (2) 0/0 - 2/4")
        Rectangle.save_to_file_csv(None)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rectangles_output), 0)
        with self.assertRaises(TypeError):
            Rectangle.load_from_file_csv(1)
        with self.assertRaises(TypeError):
            Rectangle.load_from_file_csv([r1, r2], 1)

class TestRectangle(unittest.TestCase):
    """ unittest for Rectangle class """
    def test_docs(self):
        """ tests for module docstring"""
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.__init__.__doc__) > 0)
        self.assertTrue(len(Rectangle.width.__doc__) > 0)
        self.assertTrue(len(Rectangle.height.__doc__) > 0)
        self.assertTrue(len(Rectangle.x.__doc__) > 0)
        self.assertTrue(len(Rectangle.y.__doc__) > 0)
        self.assertTrue(len(Rectangle.area.__doc__) > 0)
        self.assertTrue(len(Rectangle.display.__doc__) > 0)
        self.assertTrue(len(Rectangle.__str__.__doc__) > 0)
        self.assertTrue(len(Rectangle.update.__doc__) > 0)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 0)

    def test_init(self):
        """ tests for __init__ method """
        # test normal use
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        # test normal use
        r2 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        # test no args
        with self.assertRaises(TypeError):
            Rectangle()
        # test too many args
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)
        # test invalid type
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        # test invalid value
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)

    def test_width(self):
        """ tests for width getter and setter """
        # test normal use
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r1.width = 1
        self.assertEqual(r1.width, 1)
        # test invalid type
        with self.assertRaises(TypeError):
            r1.width = "1"
        # test invalid value
        with self.assertRaises(ValueError):
            r1.width = 0
        with self.assertRaises(ValueError):
            r1.width = -1

    def test_height(self):
        """ tests for height getter and setter """
        # test normal use
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        r1.height = 1
        self.assertEqual(r1.height, 1)
        # test invalid type
        with self.assertRaises(TypeError):
            r1.height = "1"
        # test invalid value
        with self.assertRaises(ValueError):
            r1.height = 0
        with self.assertRaises(ValueError):
            r1.height = -1

    def test_x(self):
        """ tests for x getter and setter """
        # test normal use
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)
        r1.x = 1
        self.assertEqual(r1.x, 1)
        # test invalid type
        with self.assertRaises(TypeError):
            r1.x = "1"
        # test invalid value
        with self.assertRaises(ValueError):
            r1.x = -1
    
    def test_y(self):
        """ tests for y getter and setter """
        # test normal use
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)
        r1.y = 1
        self.assertEqual(r1.y, 1)
        # test invalid type
        with self.assertRaises(TypeError):
            r1.y = "1"
        # test invalid value
        with self.assertRaises(ValueError):
            r1.y = -1

    def test_area(self):
        """ tests for area method """
        # test normal use
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        # test no args
        with self.assertRaises(TypeError):
            r1.area(1)
        # test too many args
        with self.assertRaises(TypeError):
            r1.area(1, 2)

    def test_display(self):
        """ tests for display method """
        # test normal use
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.display(), None)
        # test no args
        with self.assertRaises(TypeError):
            r1.display(1)
        # test too many args
        with self.assertRaises(TypeError):
            r1.display(1, 2)

    def test_str(self):
        """ tests for __str__ method """
        # test normal use
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        # test no args
        with self.assertRaises(TypeError):
            r1.__str__(1)
        # test too many args
        with self.assertRaises(TypeError):
            r1.__str__(1, 2)

    def test_update(self):
        """ tests for update method """
        # test normal use
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(id=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 4/5 - 2/3")

    def test_to_dictionary(self):
        """ tests for to_dictionary method """
        # test normal use
        r1 = Rectangle(10, 2, 1, 9, 111)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(type(r1_dictionary), dict)
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 111, 'height': 2, 'width': 10})
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())

class TestSquare(unittest.TestCase):
    """ unittest for Square class """
    def test_docs(self):
        """ tests for module docstring"""
        self.assertTrue(len(Square.__doc__) > 0)
        self.assertTrue(len(Square.__init__.__doc__) > 0)
        self.assertTrue(len(Square.__str__.__doc__) > 0)
        self.assertTrue(len(Square.size.__doc__) > 0)
        self.assertTrue(len(Square.update.__doc__) > 0)
        self.assertTrue(len(Square.to_dictionary.__doc__) > 0)

    def test_init(self):
        """ tests for __init__ method """
        # test normal use
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        # test normal use
        s2 = Square(2, 2, 2, 12)
        self.assertEqual(s2.id, 12)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 2)
        # test no args
        with self.assertRaises(TypeError):
            Square()
        # test too many args
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)
        # test invalid type
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        # test invalid value
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -1)
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_size(self):
        """ tests for size getter and setter """
        # test normal use
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 1
        self.assertEqual(s1.size, 1)
        # test invalid type
        with self.assertRaises(TypeError):
            s1.size = "1"
        # test invalid value
        with self.assertRaises(ValueError):
            s1.size = 0

    def test_x(self):
        """ tests for x getter and setter """
        # test normal use
        s1 = Square(5)
        self.assertEqual(s1.x, 0)
        s1.x = 1
        self.assertEqual(s1.x, 1)
        # test invalid type
        with self.assertRaises(TypeError):
            s1.x = "1"
        # test invalid value
        with self.assertRaises(ValueError):
            s1.x = -1

    def test_y(self):
        """ tests for y getter and setter """
        # test normal use
        s1 = Square(5)
        self.assertEqual(s1.y, 0)
        s1.y = 1
        self.assertEqual(s1.y, 1)
        # test invalid type
        with self.assertRaises(TypeError):
            s1.y = "1"
        # test invalid value
        with self.assertRaises(ValueError):
            s1.y = -1

    def test_str(self):
        """ tests for __str__ method """
        # test normal use
        s1 = Square(4, 6, 2, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 6/2 - 4")
        # test no args
        with self.assertRaises(TypeError):
            s1.__str__(1)
        # test too many args
        with self.assertRaises(TypeError):
            s1.__str__(1, 2)

    def test_update(self):
        """ tests for update method """
        # test normal use
        s1 = Square(10, 10, 10)
        s1.update(89)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 10")
        s1.update(89, 2)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/10 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")
        s1.update(id=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

    def test_to_dictionary(self):
        """ tests for to_dictionary method """
        # test normal use
        s1 = Square(10, 2, 1, 111)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(type(s1_dictionary), dict)
        self.assertEqual(s1_dictionary, {'x': 2, 'y': 1, 'id': 111, 'size': 10})
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1.__str__(), s2.__str__())
