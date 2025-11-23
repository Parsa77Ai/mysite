def f(L):
    
    D={}
    
    for d in L:
        
        for key in d.keys():
            
            D[key]=d.get(key)
        
    return D

d1={"apple":"sib","name":"parsa",1:3}

d2={"orange":"portegal","sen":"18",2:5}

d3={"blue":"ss","family":"oti",3:6}

a=[d1,d2,d3]

print(f(a))



