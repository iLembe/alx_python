#!/usr/bin/env python3

def raise_exception():
    raise ValueError

try:
    raise_exception()
except ValueError:
    print("Exception has been raised")
