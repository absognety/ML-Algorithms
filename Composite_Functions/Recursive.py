from sympy import *

n = int(input())
Fx = input()

Fx = simplify(Fx) #input a function of your choice with x as input variable

############# Recursive approach to composite functions ################
P = int(input())

def compositeFuncRecur(f,n,P):
    if n==0:
        return (P)
    else:
        P = compositeFuncRecur(f,n-1,f.subs({'x':P}).evalf())
        return (P)
    
print (compositeFuncRecur(Fx,n,2))