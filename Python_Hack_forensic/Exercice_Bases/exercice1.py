#!/usr/bin/env python3
# #-*-coding:UTF-8-*-

from math import *
from math import log10
size_nombre_entier= lambda x : int(log10(x))+1

def exo1_questionA (nombre1,nombre2):
    if size_nombre_entier(nombre1) == 2 and size_nombre_entier(nombre2) == 2:
        if nombre1>0 and nombre2>0:
            first_number = (int(nombre1/10)) * 1000
            second_number = nombre1%10
            resultat = first_number+(nombre2)*10+second_number
            print (resultat)
        else:
            print("L'un des deux nombres n'est pas supérieur à 0")
    else:
        print("L'un des deux nombre n'est pas un nombre de type dizaine")

def saisieInt (nombremin,nombremax):
    choice = 0
    while (choice<int(nombremin) or choice>int(nombremax)):
        print("Entrez un nombre compris entre",nombremin,"et",nombremax,": ")
        choice = int(input())

def main():
    ########################### MAIN POUR QUESTION A ET B #####################################
    #print ("########################## Question A ET B #######################################")
    #print("Choisir deux nombres entiers supérieurs à 10")
    #nombre1 = 0
    #nombre2 = 0
    #while nombre1<10 or nombre1>99 or nombre2<10 or nombre2>99:
    #    nombre1 = int(input())
    #    nombre2 = int(input())
    #exo1_questionA(nombre1,nombre2)
    ###########################################################################################

    ########################### MAIN POUR QUESTION C ET D #####################################
    print ("########################## Question C ET D #######################################")
    print("Choisir deux nombres pour constituer les nombres limites de la fonction saisieInt")
    limite_min = input("Limite minimum : ")
    limite_max = input("Limite maximum : ")
    saisieInt(limite_min,limite_max)
    


if __name__ == "__main__":
    main()
    