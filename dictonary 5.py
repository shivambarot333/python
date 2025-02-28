def dict5():
    item_master = {'manchurian': 400,'bread':50,'buttermilk':25}
    item_purchased ={'manchurian':2,'bread':4}
    total_bill_amt = 0
    for item,qty in item_purchased.items():
        total_bill_amt += item_master[item]* qty
    print ("total bill amount =", total_bill_amt)

dict5()        
