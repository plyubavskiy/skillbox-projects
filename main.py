size_list = int(input('Введите длину списка: '))

new_list = [1 if index % 2 == 0 else index % 5
            for index in range(0, size_list)]

print('Результат:', new_list)