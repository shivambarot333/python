s1= {'anand','bin','agare','atmaram','ai','bambodi'}
s2= set()
s3= set()

for x in s1:
    if x[0] == 'A' or x[0] == 'a':
        s2.add (x)
    elif x[0] == 'B' or x[0] == 'b':
        s3.add(x)

print ("values beginng with a:",s2)
print ("values beginng with b:",s3)
