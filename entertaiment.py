sticks = int(input('Кол-во палок: '))
throws = int(input('Кол-во бросков: '))

game = ['I' for i in range(sticks)]

for i in range(1, throws + 1):
    print('Бросок', i, 'Сбиты палки с номера',end = ' ')
    start = int(input())
    print('по номер',end = ' ')
    stop = int(input())
    for i_off in range (start - 1, stop):
        game[i_off] = '.'

result = ''
for i_result in game:
    result += i_result
print('\nРезультат:', result)