#!/usr/bin/env python3

# Import the specific variable 'a' from variable_load_2.py
from variable_load_2 import a

if __name__ == "__main__":
    if a == 89:
        print("89")
    elif a == -100:
        print("-100")
    else:
        print("Traceback (most recent call last):")
