nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_nice_list = [x for y in nice_list for a in y for x in a]
print(new_nice_list)

# for y in nice_list:
#     print(y)
#     for a in y:
#         print(a)
#         for x in a:
#             print(x)