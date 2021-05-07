# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:12:38 2021

@author: Félix
"""
from random import *
encorebesoinR=True
while encorebesoinR==True:
    print('MENU')    
    print("1-Cryptage en morse")
    print("2-Décryptage de Morse")
    print("3-Fin du programme")

    choix=int(input('Quel est votre choix ?'))   
    assert type(choix)==int,'Le nombre doit être entier'   
    assert choix<=3 and choix>=1,'Veuillez choisir une des 3 possibilité'  
    alphabetmin=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
    alphabetmaj=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if choix==1:

        texte=str(input('Quel est le texte a crypter ?'))  

        texteCrypteR=str()
        def defcleR(alphabetmin):
            cleR=''
            hasacle = randint(1,4)
            for i in range(hasacle):
                cleR += alphabetmin[randint(0,25)]
            return cleR
        def cryptageR(texte,alphabetmin):
            nouvTexte = ''
            for a in texte:
                nouvTexte+= a.upper()

            
            out = ''
            cleR = defcleR(alphabetmin)
            for lettre in nouvTexte:
                bon = False
                while bon==False:
                    hasa = randint(0,30)
                    if hasa == 26:
                        out += lettre
                        bon = True
                    elif hasa >= 27:
                        out += cleR
                        out += alphabetmaj[randint(0,25)]                                      
                    else:
                        out += alphabetmin[hasa]
            print("cle de", cleR)
            return out
        


        
                
        print(cryptageR(texte,alphabetmin))

        
    if choix==2:
        texte=str(input('Quel est le texte a décrypter ?'))
        cleR = str(input("Quelle est la clé ?"))


        

        
        def decryptageR(texte,cleR):
            out = ''
            justeavant = []
            taille = len(cleR)
            for lettre in texte:
                
                if taille < len(justeavant):
                    justeavant.pop(0)
                    
                if lettre.isupper():
                    justeavantStr = ''
                    for c in range(taille):
                        justeavantStr += str(justeavant[c])
                    
                    if justeavantStr != cleR:
                        out += lettre
                elif lettre.isspace():
                    out += lettre
                else:
                    out = out
                justeavant.append(lettre)
            return out

        texteDecrypteR= decryptageR(texte,cleR)

        
        print(texteDecrypteR)
        
        

    if choix==3:
        print("Fin du programme")
        encorebesoinR=False