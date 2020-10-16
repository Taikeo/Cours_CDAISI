#!/usr/bin/env python3 
# #-*-coding:UTF-8-*-

def is_palindrome(chaine):
    if chaine == chaine[::-1]:
        print(chaine,"est un palindrome")
    else: 
        print(chaine,"n'est pas un palindrome")



    
is_palindrome("KAYAK")