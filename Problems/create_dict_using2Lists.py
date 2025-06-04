#Create a dictionary from two lists: one of keys and one of values. Then print the dictionary.
#(Example: keys = ['a', 'b'], values = [1, 2] → { 'a': 1, 'b': 2 })


keys = input("Enter the keys: ").split()
values = list(map(int, input("Enter the values: ").split()))

if len(keys) != len(values):
    print("Invalid input! Keys and values must be the same length.")
else:
    my_dict = {}
    for i in range(len(keys)):
        my_dict[keys[i]] = values[i]

    print(my_dict)
