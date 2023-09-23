"""


There should be a docString here



"""
#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.__size = size

if __name__ == "__main__":
    mysquare = Square(3)
    print(type(mysquare))

    try:
        print(mysquare.__dict__)
    except Exception as e:
        print(e)

