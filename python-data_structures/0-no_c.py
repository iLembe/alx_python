def no_c(my_string):\n    new_string = ""\n    for char in my_string:\n        if char.lower() != "c":\n            new_string += char\n    return new_string\n\n# Example usage:\nmy_string = "Hello, World! C is Fun!"\nresult = no_c(my_string)\nprint(result)  # Output: "Hello, World!  is Fun!"
