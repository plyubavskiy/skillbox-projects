import random

num_list = [random.randint(-1, 1) for _ in range(15)]
print(num_list)
num_list0 = [x for x in num_list if x == 0]
num_list2 = [x for x in num_list if x != 0]
num_list3 = num_list2 + num_list0 # не понял зачем, но по условию задачи это нужно действие

print(num_list2)