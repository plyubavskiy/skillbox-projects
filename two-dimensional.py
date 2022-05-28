# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

x = 4
num_list = [list(range(y, (y + x) * 2 - y + 1, x)) for y in range(1, x + 1)]
print(num_list)
