def concdict():
    d1={0:'zero',1: 'one', 2: 'two'}
    d2 ={3:'three', 4: 'four' ,5: 'five'}
    d3={6: 'six', 7 :'seven', 8: 'eight'}
    d4={**d1, **d2,**d3}
    n= int(input("enter a no.(0..9)"))
    print(n,d4[n])
concdict ()   
