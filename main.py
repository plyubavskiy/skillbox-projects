volwers = 'аеёиоуыэюя'

text = input('Введите текст: ')
search_volwers = [vol for vol in text if vol in volwers]

print('\nСписок гласных букв:', search_volwers)
print('Длина списка:', len(search_volwers))