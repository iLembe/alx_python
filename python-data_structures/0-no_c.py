def no_c(my_string):\n    new_string = ""\n    for char in my_string:\n        if char.lower() != "c":\n            new_string += char\n    return new_string\n\nprint(no_c("Coding is fun!"))
