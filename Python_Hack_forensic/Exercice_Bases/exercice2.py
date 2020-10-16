#!/usr/bin/env python3 
# #-*-coding:UTF-8-*-

from math import *

def absolute_number (nombre):
    print (abs(nombre))

def solveur_affine (a,b):
    print ("==================== SOLVEUR D'ÉQUATION AFFINE =======================")
    if a != 0:
        result = -b/a
    else:
        if b == 0:
            result = "indéterminé"
        else:
            result = "impossible"
    print ("Le resultat est ",result)


def delta_calculator (a,b,c):
    return int(pow(2,b)-4*a*c)

def solveur_seconde_degre (a,b,c):
    delta = delta_calculator(a,b,c)
    print ("==================== SOLVEUR D'ÉQUATION DU SECOND DEGRE =======================")
    print ("delta = ",delta)
    if delta > 0:
        sqrtdelta = sqrt(delta)
        result = [(-b-sqrtdelta)/(2*a),(-b+sqrtdelta)/(2*a)]
    elif delta < 0:
        result = []
    else:
        result = [-b/(2*a)]
    print("Il y a",len(result),"solutions possibles")
    print("Le résultat est",result)

def is_equilateral(cote1,cote2,cote3):
    if (cote1==cote2==cote3):
        return True
    return False

def is_isocele(cote1,cote2,cote3):
    if (cote1==cote2 or cote2==cote3 or cote1==cote3):
        return True
    return False

def is_rectangle(cote1,cote2,cote3):
    if (cote1*cote1==cote2*cote2+cote3*cote3 or cote2*cote2==cote1*cote1+cote3*cote3 or cote3*cote3==cote2*cote2+cote1*cote1)

def is_type(a,b,c):
    if is_isocele(a,b,c):
        return "Isocele"
    elif is_equilateral(a,b,c):
        return "Equilateral"
    elif is_rectangle(a,b,c):
        return "Rectangle"
    else:
        return "Quelconque"

def main():
    a = int(input("Valeur du coefficient a: "))
    b = int(input("Valeur du coefficient b: "))
    c = int(input("Valeur du coefficient c: "))
    solveur_affine(a,b)
    solveur_seconde_degre(a,b,c)
    longueur1 = float(input("Valeur de la longueur1: "))
    longueur2 = float(input("Valeur de la longueur2: "))
    longueur3 = float(input("Valeur de la longueur3: "))
    print("Le triangle de valeur",[longueur1,longueur2,longueur3],"est un triangle",is_type(longueur1,longueur2,longueur3))


if __name__ == "__main__":
    main()
