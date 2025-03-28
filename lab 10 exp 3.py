import random
random_numbers = set()
while len(random_numbers)  < 10:
      random_numbers.add(random.randint (-15,15))
print (random_numbers)


def square(n):
    return n*n


print(list(map(square,random_numbers)))
