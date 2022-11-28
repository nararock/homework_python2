month = int(input('Введите номер месяца: '))

# Решение 1 со словарем
dict_seasons = \
    {
        "зима": [12, 1, 2],
        "весна": [3, 4, 5],
        "лето": [6, 7, 8],
        "осень": [9, 10, 11]
    }

find_season1 = None
for elem in dict_seasons.items():
    if find_season1:
        break
    for find_m in elem[1]:
        if month == find_m:
            find_season1 = elem[0]
            break

print(f'Решение со словарем: ваш сезон года - {find_season1}')

# Решение 2 со списком
list_seasons = [("зима", (12, 1, 2)), ("весна", (3, 4, 5)),
                ("лето", (6, 7, 8)), ("осень", (9, 10, 11))]

find_season2 = None
for elem in list_seasons:
    if find_season2:
        break
    for find_m in elem[1]:
        if month == find_m:
            find_season2 = elem[0]
            break

print(f'Решение со списком: ваш сезон года - {find_season2}')
