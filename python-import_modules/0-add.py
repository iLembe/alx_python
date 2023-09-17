#!/usr/bin/env python3

def add_0(a, b):
    """Adds two integers and returns the result."""
    return a + b

if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add_0(a, b)))
