import random
def List2():
    lst = [random.randint(1,100) for x in range(20)]
    print(lst)
    x= int(input("ENTER A NO."))
    p= -1
    NotFound = False
    for i in lst:
         p= p+1
    if i == x:
            print(x, "found at",p)
            Found = True
    if found == False:
       print(x," is not there in the list.")     

List2()
List2()
