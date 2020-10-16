#!/usr/bin/env python3
# #-*-coding:UTF-8-*-

import os
import re
import socket

############################################Création des fichiers textes (pour simplifier)####################################################
def creation_fichier():
    for i in range (4):
        fichier = "fichier{}.txt".format(i+1)
        opened=open(fichier,'w')
        opened.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. In imperdiet in urna in efficitur. Quisque turpis lorem, vulputate non augue sed, commodo facilisis ligula. Vivamus blandit arcu quis nulla mollis tempus. Suspendisse quis ex vitae metus viverra ullamcorper. Nunc eu nibh ac ex consequat eleifend. Morbi sollicitudin quis neque a blandit. Morbi vel orci mollis, sollicitudin arcu vitae, facilisis metus. Etiam a neque id tortor congue iaculis. Sed tincidunt urna augue, congue fermentum libero gravida vel. Aenean finibus bibendum felis, eget viverra leo dapibus in.")
###############################################################################################################################################

#####################################################Recherche des fichiers .TXT###############################################################
def recherche_txt(path):
    regex = re.compile('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}')
    for root,dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".txt"):
                fullpath = os.path.join(root,f)
                opened = open(fullpath,'r')
                resultat = regex.findall(opened.read())
                return resultat

#recherche_txt('/Users/kevintaikeo/Documents/Cours_CDAISI/Python_HackingForensic/')
###############################################################################################################################################

#####################################################Recherche des fichiers .JPG###############################################################
def recherche_jpg(path):
    print("==================Listes des fichiers JPG=================")
    for root,dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".jpg"):
                if not os.path.exists(path+"TP1/recherche_jpg"):
                    os.mkdir(path+"TP1/recherche_jpg")
                fullpath = os.path.join(root,f)
                os.system("cp "+fullpath+" /Users/kevintaikeo/Documents/Cours_CDAISI/Python_HackingForensic/TP1/recherche_jpg/")
                fullpath = re.sub(r'\.jpg$','',fullpath)
                print(fullpath)
                

#recherche_jpg('/Users/kevintaikeo/Documents/Cours_CDAISI/Python_HackingForensic/')
###############################################################################################################################################

#####################################################Détermination adresse IP##################################################################
def find_our_ip():
    ip = socket.gethostbyname(socket.gethostname())
    ip_lan = ip.split(".")
    ip_lan.pop()
    ip_lan =".".join(ip_lan)
    return ip

def find_our_ip_lan(ip):
    ip_lan = ip.split('.')
    ip_lan.pop()
    ip_lan =".".join(ip_lan)
    return ip_lan

#find_our_ip()
#find_our_ip_lan()
###############################################################################################################################################

#####################################################RECHERCHE SI DANS LE MÊME LAN ET TRIÉE###################################

def sort_results(resultat):
    for i,elt in enumerate(resultat):
        if not find_our_ip_lan(resultat[i]) == find_our_ip_lan(find_our_ip()):
            del resultat[i]
    return resultat

#resultat = recherche_txt('/Users/kevintaikeo/Documents/Cours_CDAISI/Python_HackingForensic/')
#print(resultat)
#sort_results(resultat)
###############################################################################################################################################

def main():
    path = input("Entrez le chemin pour effectuer les fonctions: ")
    liste = recherche_txt(path)
    print("\n")
    recherche_jpg(path)
    our_ip = find_our_ip()
    print("\nNotre adresse IP:",our_ip)
    print("\nAdresses IP du même lan:",sort_results(liste))
    #sort_results(liste)

if __name__ == "__main__":
    main()
    