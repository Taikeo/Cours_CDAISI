#!/usr/bin/env python3 
# #-*-coding:UTF-8-*-

def occurence(liste,valeur):
    for i,elt in enumerate(liste):
        if (elt == valeur):
            print(i) 
            break
    else:
        print(-1)

def occurence_trie(liste,valeur):
    for i,elt in enumerate(liste):
        if elt == valeur:
            print ("Arrêt à l'indice",i,"sur",len(liste))
            break
        elif elt>valeur:
            print(-1)
            print ("Arrêt à l'indice",i,"sur",len(liste))
            break



def dichotomie(liste,valeur):
    index=0
    longueur = len(liste)
    if longueur == 0:
        print("Liste vide -> -1")
    while longueur > index+1:
        middle = (index+longueur)//2
        if liste[middle] > valeur:
            longueur = middle
        else:
            index = middle
    return index

def nb_occurence(liste,valeur):
    cpt=0
    for elt in liste:
        if elt == valeur:
            cpt+=1
    print("Nombre d'occurence de",valeur,"dans la liste :",liste,":",cpt)

def nb_occurence_trie(liste,valeur):
    cpt=0
    for i,elt in enumerate(liste):
        if elt == valeur:
            cpt+=1
        elif elt>valeur:
            print("Arrêt à l'indice",i,"sur",len(liste),"élement")
            break
    print("Nombre d'occurence de",valeur,"dans la liste :",liste,":",cpt)

def nb_max_and_min_liste(liste):
    max=liste[0]
    min=liste[0]
    for elt in liste:
        if elt>max:
            max = elt
        if elt<min:
            min = elt
    print("Le minimum de la liste est :",min,"\nLe maximum:",max)
        
def nb_max_and_min_liste_trie(liste):
    max=liste[len(liste)-1]
    min=liste[0]
    print("Le minimum de la liste est :",min,"\nLe maximum:",max)

def moyenne_liste(liste):
    for elt in liste:
        moyenne+=elt
    moyenne/=len(liste)
    print("moyenne :",moyenne)

def add_liste(liste1,liste2):
    tmp=[]
    for i,elt in enumerate(liste1):
        tmp.append(liste1[i]+liste2[i])
    print(tmp)

def doublon_liste(liste):
    tmp=[]
    for i,elt in enumerate(liste):
        if elt not in tmp:
            tmp.append(elt)
    print("Ancienne liste :",liste,"\nNouvelle liste :",tmp)

def same_in_liste(liste1,liste2):
    tmp=[]
    if len(liste1)>len(liste2):
        max = sorted(liste1)
        min = sorted(liste2)
    else:
        max = sorted(liste2)
        min = sorted(liste1)
    for i,elt in enumerate(max):
        if elt in min:
            tmp.append(elt)
    print("Valeurs communes aux deux listes :",tmp)

def not_same_in_liste(liste1,liste2):
    tmp=[]
    if len(liste1)>len(liste2):
        max = sorted(liste1)
        min = sorted(liste2)
    else:
        max = sorted(liste2)
        min = sorted(liste1)
    for i,elt in enumerate(max):
        if elt not in min:
            tmp.append(elt)
    print("Valeurs différentes aux deux listes :",tmp)

#nb_max_and_min_liste([1,3,50,3,54,3])
#nb_max_and_min_liste_trie(sorted([1,3,50,3,54,3]))

#moyenne_liste([1,1,1,1,2])
#add_liste([1,1,1,1,2],[1,1,1,1,2])
#doublon_liste([1,1,1,1,2,4,3,2,3,4])
#same_in_liste([1,1,1,1,2],[1,1,1,1,2,4,3,2,3,4])
not_same_in_liste([1,1,1,1,2],[1,1,1,1,2,4,3,2,3,4])

#occurence_([2,3,4,5,6,8],7)
#occurence_trie([2,3,4,5,6,8],7)
#nb_occurence([1,3,4,2,3,4,2,2],2)
#nb_occurence_trie(sorted([1,3,4,2,3,4,2,2,2]),2)
#dichotomie([1,2,3,5],3)
#a=dichotomie([1,2,3,5],3)
#print(a)