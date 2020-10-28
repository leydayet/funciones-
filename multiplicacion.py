import math 

def adentro(a,b,c):
    operacion = pow(b,2)-(4*a*c)
    return operacion

def raices(a,b,operacion):
     raiz1 = (-b+math.sqrt(operacion))/(2*a)
     raiz2 = (-b-math.sqrt(operacion))/(2*a)
     return raiz1,raiz2
print ('calcular las raices')
a=float(input('ingrse A'))
b=float(input('ingrse B'))
c=float(input('ingrse C'))
operacion =adentro(a,b,c)
if operacion <=0:
    print('no hay raices positivas')
else:
    print('las raices son:')
    impimir = raices(a,b,operacion)
    #raices(a,b,operacion)
    print (impimir)