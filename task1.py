my_list = \
    [
        1, 'word', True, ['new_list', 2.5],
        None, ('tuple', 3), 4.5,
        {'a', 1, 1, 'a'}, {'k1': 1, 'k2': 2}
    ]

for el in my_list:
    print(f"{el} - {type(el)}")
