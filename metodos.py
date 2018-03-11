# ----------------------------- IMPLEMENTAÇÕES CODESCHOOL ---------------------------------------

#MÉTODO DA BISSEÇÃO -----------------------------------------------------------------------------

import math

#Lê número de iterações

n = int(input("n: "))

#Define a função

def f(x):
    return x - math.cos(x) - 4
    
#Define o intervalo inicial 
x0,x1  = 0,10


if f(x0)<f(x1) :
    xa,xb = x0,x1
else:
    xa,xb = x1,x0

for i in range (n):
    xmedio = (xa+xb)/2
    
    if f(xmedio) <= 0 :
        xa = xmedio;
    else:
        xb = xmedio;
    print("%.3f, %.3f" %(xa,xb))
if abs(f(xa))< abs(f(xb)):    
    resposta = xa
else: 
    resposta = xb
print (resposta)

#MÉTODO DA FALSA POSIÇÃO -------------------------------------------------------------------------

import numpy as np

#definindo a função 

def f(x):
    return np.cos(x/2) 

#define intervalo inicial

x0, x1 = 3,4

n = int(input("Número de iterações : "))

# condiciona limites do intervalo

if f(x0)<f(x1):
    xa , xb = x0,x1
else :
    xa,xb = x1,x0

for i in range(n):
    xfalso = (xa*f(xb) - xb * f(xa))/(f(xb)-f(xa))
    if f(xfalso) <=0 :
        xa = xfalso
    else:
        xb = xfalso
        
#Checa qual a melhor resposta
if abs(F(xa))< abs(F(xb)):
    resposta = xa
else :
    resposta = xb
print(resposta)

#MÉTODO DE NEWTON - RAMPSON -------------------------------------------------------------------------    

import math

#DEFINE PONTO INICIAL

x = int(input("x: "))

#DEFINE NUMERO DE INTERACOES
n = int(input("n: "))

#DEFINE FUNÇÃO E SUA DERIVADA
def f(x):
    return x-math.cos(x)
def f_(x):
    return 1+math.sin(x)
#EXECUTA AS INTERAÇÕES
for i in range(n):
    x = x - f(x)/f_(x)
    
print("%.4f" %(x)) 

#MÉTODO DA SECANTE ------------------------------------------------------------------------- 

import numpy as np

#definindo a função 

def f(x):
    return np.cos(x/2) 

#define intervalo inicial

xa, xb = 0,5

n = int(input("Número de iterações : "))

for i in range(n):    
    x = xb - ((f(xb)/(f(xb)-f(xa)))* (xb-xa))
    xa = xb
    xb = x
    if( abs(f(x))<0.0000001):
        break
print(x)

#MÉTODO PONTO FIXO ------------------------------------------------------------------------- 