import random


odd_list = random.sample(range(1, 100, 2), 5)
even_list = random.sample(range(0, 100, 2), 4)

print("Odd list:", odd_list)
print("Even list:", even_list)


odd_list[2:3] = even_list
print("Modified list:", odd_list)


odd_list.sort()
print("Sorted list:", odd_list)
