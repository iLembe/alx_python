#!/usr/bin/env python3

def raise_exception_msg(message=""):
    if message:
        raise NameError(message)
    else:
        raise NameError

raise_exception_msg("Python is cool")
raise_exception_msg("C is fun")
#raise_exception_msg("")
