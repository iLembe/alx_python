"""
A docstring is needed here

"""
#!/usr/bin/python3
def is_same_class(obj, a_class):
    """"
A DocString
"""   
    return type(obj) is a_class


a = ""
result = is_same_class(a, int)
print("", file=open("NUL", "w"))
