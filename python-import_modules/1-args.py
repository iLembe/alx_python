#!/usr/bin/env python3

from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    args = argv[1:]

    print(f"Number of argument(s): {num_args}", end="")
    if num_args == 0:
        print(".")
    elif num_args == 1:
        print(f"\\nArgument 1: {args[0]}")
    else:
        print(":")
        for i, arg in enumerate(args, start=1):
            print(f"Argument {i}: {arg}")
