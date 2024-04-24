#!/usr/bin/python3
"""This model defines a square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the square class that inherits from
    the rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance of the square class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Changes the printable version of rectangle"""

        string = "[Square] ({}) {}/".format(self.id, self.x)
        string2 = "{} - {}".format(self.width)
        total_string = string + string2

        return total_string

    @property
    def size(self):
        """Returns the value of size"""
        return self.width

    @size.setter
    def size(self, size):
        """sets the value of size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the attribute for the rectangle class"""

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

        if len(args) > 0:
            self.id = args[0]

        if len(args) > 1:
            self.width = args[1]

        if len(args) > 2:
            self.x = args[2]

        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""

        initial_dict = self.__dict__
        new_dict = {}

        for key, value in initial_dict.items():
            if key.startswith("_Rectangle__"):
                new_key = key.replace("_Rectangle__", "")
                new_dict[new_key] = value
            else:
                new_dict[key] = value
        new_dict["size"] = new_dict["width"]
        del new_dict["width"]
        del new_dict["height"]
        return new_dict
