amount = int(input('Введите количество товаров: '))
my_list = []
for element in range(amount):
    my_dict = \
        {
            'название': input('Введите название товара: '),
            'цена': input('Введите цену товара: '),
            'количество': input('Введите количество товара: '),
            'ед': 'шт.'
        }
    my_list.append((element + 1, my_dict))

for el in my_list:
    print(el)

dict_product = \
    {
        'название': [],
        'цена': [],
        'количество': [],
        'ед': []
    }
for element in my_list:
    for el in element[1].items():
        dict_product[el[0]].append(el[1])

for elem in dict_product.items():
    print(f'{elem[0]}: {set(elem[1])}')
