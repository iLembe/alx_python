#!/usr/bin/python3
"""Module for the Square class, which inherits from Rectangle."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class, inherits from Rectangle."""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x-coordinate of the square (default is 0).
            y (int): The y-coordinate of the square (default is 0).
            id (int): The id of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
