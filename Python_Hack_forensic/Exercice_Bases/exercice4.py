#!/usr/bin/env python3
# #-*-coding:UTF-8-*-

def xn_iteratif(n):
    for x in range (n):
        print(x**n)

xn_iteratif(25)

def algo(x,n):
    while n > 0:
        x *= x
        n -= 1
        print(x)

def algo_rec(x,n):
    return x if n == 0 else algo_rec(x*x, n-1)
algo(5,5)

def is_premier(n):
    if n <= 2:
        return True if n == 2 else False
    for i in range (2,n):
        if n%i == 0:
            return False
        return True

#a=is_premier(2)
#print(a)

def listPremier(n):
    a = []
    for n in range(0,n):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    break
            else:
                a.append(n)
    return a
#liste=listPremier(100)
#print(liste)