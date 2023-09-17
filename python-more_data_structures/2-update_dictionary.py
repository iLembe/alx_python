def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value

def print_sorted_dictionary(my_dict):
    sorted_keys = sorted(my_dict.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, my_dict[key]))

a_dictionary = {}
update_dictionary(a_dictionary, 'a', 'a')

print_sorted_dictionary(a_dictionary)
print("xx")

update_dictionary(a_dictionary, 'a', 'a')
print_sorted_dictionary(a_dictionary)
