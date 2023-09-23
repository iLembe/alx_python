"""
A docstring is needed here

"""
#!/usr/bin/python3

#!/usr/bin/python3

class BaseGeometry:
    """Empty class for BaseGeometry."""

    def area(self):
        """Method to calculate the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate integers.

        Args:
            name (str): The name of the attribute.
            value (int): The value to validate.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string in the format [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

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
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
