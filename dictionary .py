def dict3():
    empdata ={('ce',77):50000,('ce',103):55000,('design',169):40000,('product',167):50000,('design',184):8000}
    deptdata ={}
    for k,v in empdata .items():
        print (k[0], k[1],v)
        if k[0] not in deptdata:
            deptdata[k[0]] = {'max':v,'min':v, 'total':v}
        else:
             if v > deptdata[k[0]]['max']:
                 deptdata [k[0]]['max'] =v
             elif v < deptdata[k[0]]['min']:
                deptdata [k[0]]['min'] =v
             deptdata [k[0]]['total']+=v
        print(deptdata)
dict3()
                          
