import random
odd=[random.randint(1,1000) * 2 - 1 for _ in range(5)]
print("odd numbers are",odd)
even=[random.randint(1,1000) * 2 for _ in range(4)]
print("even number are:",even)
odd[2] = even
print("after replace",odd)
