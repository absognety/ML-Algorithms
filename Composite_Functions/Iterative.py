from sympy import *

n = int(input())
Fx = input()

Fx = simplify(Fx) #input a function of your choice with x as input variable
############# Iterative approach to composite functions ################
P = int(input())

def compositeFunc(f,n,P):
    if n == 0:
        return (P)
    else:
        while (n > 0):
            P = f.subs({'x':P})
            n -= 1
        return (P)

print (compositeFunc(Fx,n,2))