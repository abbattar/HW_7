print('Начальное выражение', data := [1,2,2,3,5,6,6,7,9,0,11,12,12])
print(('Уникальные', [n for n in set(data) if data.count(n) == 1]))
print('Повторяемые', [ n for n in set(data) if data.count(n) > 1])  # Операция [list1] - [list2] не существует
print('Без дубликатов', list(set(data)))