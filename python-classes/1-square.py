"""Initialize a square.

 Args:
    size (int): The size of the square (default 0).
"""
#!/usr/bin/python3

class Square:
    """Initialize a square.

 Args:
    size (int): The size of the square (default 0).
"""
    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): The size of the square (default 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

if __name__ == "__main__":
    try:
        my_square = Square(3)
        print("Size:", my_square.__dict__["_Square__size"])
    except Exception as e:
        print(e)
