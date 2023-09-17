def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key].append(value)
    else:
        a_dictionary[key] = [value]

for k, v in a_dictionary.items():
    print(f"{k}: {v}")

print("xx") 