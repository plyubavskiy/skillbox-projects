import random

squad_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
squad_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [squad_1[index] if squad_1[index] > squad_2[index]
           else squad_2[index] for index in range(len(squad_1))]

print('Первая команда:', squad_1)
print('Вторая команда:', squad_2)
print('Победители:', winners)