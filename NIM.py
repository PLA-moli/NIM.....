# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:45:36 2023

@author: JINCHENYI
"""

from math import *
from random import *
def computer(n):
    #la partie de la ordinateur
    po=[]
    god=n//2-1
    for i in range(0,int(log2(n))+1):    #touts les nombre petit que n,la nombre carré de 2 -1 rentré dans  le liste de range
        c=2**(i+1)-1
        po.append(c)
    while True:
        num=choice(po)                 #Choisissez un nombre au hasard dans la liste
        d=n-num                       #d c'est le nombre de alumette L'ordinateur a pris
        if 0<d<=n//2 and n not in po:          #Filter pour le nombre de critères qui correspond
            print("L'ordinateur a emporté {} allumettes".format(d))
            return d
        elif n in po:                  #nombre simple c'est le carré de 2 -1，npc Prenez un nombre aléatoire 
            m=randint(1,god+1)
            print("L'ordinateur a emporté {} allumettes".format(m))
            return m
        else:
            continue
def person(n):
    print("=================*****JEU DE NIME*****=================")
    #Rond de joueur
    while n>1:
        print("Mainrenant,il y a {} allumette".format(n))
        while True:
            try:
                num =int(input("entrer le nombre de allumettes que vous souhaitez prendre："))
                assert 1<=num <=n//2                              #assures qu le numéros que vous entrez sont conformes aux règles du jeu
                break
            except:
                print("Entrez un nombre de 1 à {}".format(n//2))
        n-=num
        if n==1:
            return 'Gagné'
        #rond de l'ordinateur
        n-=computer(n)
    else:
        return 'Perdu'
def main():
    print(person(randint(1,100)))      #Sélectionnez au hasard le nombre total et démarrez le jeu
    while True:
        try:
            continue1=input("vous voudrez continuez?entrez YES pour continuer，entrez NO pour quitter:")
            assert continue1=='yes' or continue1=='no'
            if continue1=='no':
                print("BYE！！！")
                break
            elif continue1=='yes':
                print(person(randint(1,100)))
        except:
            print("entre yes ou no")
if __name__=='__main__':
    main()