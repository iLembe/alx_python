"""
A docstring is needed here

"""
#!/usr/bin/python3

from importlib import import_module

module_name = '5-base_geometry'
module = import_module(module_name)
BaseGeometry = module.BaseGeometry



class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If width or height is not a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
