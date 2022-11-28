user_string = input('Введите строку: ')

user_list = user_string.split(' ')
for ind, elem in enumerate(user_list):
    print(ind + 1, elem[:10])
