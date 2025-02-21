import random
s={random.randint (15,45) for _ in  range(10)}
print ("set:",s,"i < 30 ", sum (n <30 for n in s))
s= {n for n in s if n < 36}
print ("new  set :",s)
