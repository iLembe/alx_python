"""
A docstring is needed here

"""
#!/usr/bin/python3

class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Calculate the area of a geometry object.

        Raises:
            Exception: This method should be implemented in derived classes.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
