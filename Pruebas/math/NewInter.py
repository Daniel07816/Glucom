import numpy as np
import sympy as sym

def Newton(time,gluco,int):
    a=[]
    divDIF=[]
    if len(time) == len(gluco):
        n=len(time)
        a=[]
        a.append(gluco[0])

        divDIF = []
        divDIF.append([])
        for i in range (n-1):  
            divDIF[0].append((gluco[i+1]-gluco[i])/(time[i+1]-time[i]))
        
        for j in range (1,n-1):
            for i in range (0,n-j-1):
                if i == 0: 
                    divDIF.append([])
                
                divDIF[j].append((divDIF[j-1][i+1]-divDIF[j-1][i])/(time[j+i+1]-time[i]))

        for j in range (0,n-1):
            a.append(divDIF[j][0])
        
        x=sym.Symbol('x')

        y=a[0]
        for i in range (1,len(a)):
            t=a[i]
            for j in range(i):
                t=t*(x-chinga[j])
            y+=t
            
        return y
    else:
        return 0

#Prueba
x=sym.Symbol('x')
chinga=[1,2,4,5,7]
damadre=[52,5,-5,-40,10]
a=Newton(chinga,damadre,9)
print(a.subs(x,9))

"""
x=sym.Symbol('x')

fx=a[0]
for i in range (1,len(a)):
    t=a[i]
    for j in range(i):
        t=t*(x-chinga[j])
    y+=t

print(y)
print(y.subs(x,9))
"""