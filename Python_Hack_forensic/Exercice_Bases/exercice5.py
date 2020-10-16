#!/usr/bin/env python3 
# #-*-coding:UTF-8-*-

def recur_fibo(n):
    if n <= 1:
        return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

def fibo(n):
    print("=========Fibonacci=========")
    for i in range(n):
       print(recur_fibo(i))

fibo(10)