def compute(no):
    s = 0
    for i in range(1,5):
        s += int(no *i )
    return s

for x in range(4,8):
    print(compute(str(x)))
