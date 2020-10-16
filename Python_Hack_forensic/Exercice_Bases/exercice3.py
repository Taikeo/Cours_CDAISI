#!/usr/bin/env python3
# #-*-coding:UTF-8-*-

def multi_table():
    print("=================================TABLE DES MULTIPLICATIONS================================")
    for x in range(-1, 11):
        x = 'X' if x == -1 else x
        print(x, end='\t')
        for y in range(0, 11):
            if x != 'X':
                print(y*x, end='\t')
            else:
                print(y, end='\t')
        print("\n")
#multi_table()

def alternativ(c):
    print("=========Alternative * .=========")
    for i in range (0,c):
        print('*' * (c - i) + ('.' * i))

alternativ(6)

