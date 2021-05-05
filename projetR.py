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
        def defcle(alphabetmin):
            cle=''
            hasacle = randint(1,4)
            for i in range(hasacle):
                cle += alphabetmin[randint(0,25)]
            return cle
        def cryptageR(texte,alphabetmin):
            nouvTexte = ''
            for a in texte:
                nouvText+= a.upper()

            
            out = ''
            cle = defcle(alphabetmin)
            for n in texte:
                bon = False
                while bon==False:
                    hasa = randint(0,30)
                    if hasa == 26:
                        out += lettre
                        bon = True
                    elif hasa >= 27:
                        out += cle
                        out += alphabetmaj[randint(0,25)]                                      
                    else:
                        out += alphabetmin[hasa]
            print("cle de", cle)
            return out
        


        
                
        print(cryptageR(texte,alphabetmin))

        
    if choix==2:
        texte=str(input('Quel est le texte a décrypter ?'))
        texteDecrypteR=str()

        

        
        def decryptageR(lettre,cle):
            if lettre.isupper() or lettre.isspace():
                return lettre
            else:
                return ''
            

        for symb in texte:
            texteDecrypteR+=decryptageR(symb)

        
        print(texteDecrypteR)
        
        

    if choix==3:
        print("Fin du programme")
        encorebesoinR=False