def count_lower_upper(str):
    alpha = {'u':0,'l':0}
    
    for x in str:
        if x.isupper() == True :
            alpha['u'] += 1
        elif x.islower() == True :
            alpha['l'] += 1
    return alpha 








str=input("enter the string:")
print(count_lower_upper(str))
