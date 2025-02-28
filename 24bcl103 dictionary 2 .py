def dict2(d):
    if len(d)==0:
        print("the dictonary is empty")
    else:
        print("the dictonary is not empty")
    print("not empty" if bool(d)==True else "empty" )
    print("not empty" if bool(d) else "empty")

d2={}
dict2(d2)
