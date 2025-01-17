def major_minor() :
    age = int(input ("enter your age"))
    if age < 18 :
        print("you are still minor.")
    else:
        print("you have become major , now.")

    print("minor") if age < 18 else print ("major") 


major_minor()        
major_minor()
