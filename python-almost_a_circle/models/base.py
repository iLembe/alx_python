#!/usr/bin/python3
"""Base class for managing id attribute in all other classes."""

class Base:
    
    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for Base.

        Args:
            id (int): The id value (default is None).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
