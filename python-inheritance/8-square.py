"""
A docstring is needed here

"""
#!/usr/bin/python3

from importlib import import_module

module_name = '7-rectangle.py'
module = import_module(module_name)
Rectangle = module.Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is not a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: A string in the format [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__width, self.__height)
