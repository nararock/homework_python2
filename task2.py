size = int(input('Введите размер списка: '))

my_list = []
for i in range(size):
    my_list.append(input(f'Введите {i} элемент  списка: '))

print(f'было: {my_list}')

for i in range(size - 1):
    if i % 2:
        continue
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(f'стало: {my_list}')
