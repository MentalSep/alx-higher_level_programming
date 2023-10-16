#!/usr/bin/python3
"""This module contains the Base class"""
import json


class Base:
    """This is the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the initialization method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**x) for x in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**x) for x in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangles and squares"""
        import turtle

        turtle.bgcolor("grey")
        turtle.speed(5)

        for rect in list_rectangles:
            turtle.color("red")
            turtle.pu()
            turtle.setpos(rect.x, rect.y)
            turtle.pd()
            for i in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
            turtle.end_fill()

        for square in list_squares:
            turtle.color("black")
            turtle.pu()
            turtle.setpos(square.x, square.y)
            turtle.pd()
            for i in range(2):
                turtle.forward(square.width)
                turtle.left(90)
                turtle.forward(square.height)
                turtle.left(90)

        turtle.exitonclick()
