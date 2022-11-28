my_list1 = [7, 5, 3, 3, 2]
number = int(input('Введите число: '))

# Решение 1
my_list1.append(number)
my_list1 = sorted(my_list1, reverse=True)
print(f'решение1: {my_list1}')

# Решение 2
my_list2 = [7, 5, 3, 3, 2]
counter = 0
min_element = min(my_list2)
if number < min_element:
    my_list2.append(number)
else:
    for el in my_list2:
        counter += 1
        if el < number:
            my_list2.insert(counter - 1, number)
            break
print(f'решение2: {my_list2}')
