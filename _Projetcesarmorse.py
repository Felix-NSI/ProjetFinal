# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:33:36 2021

@author: Félix 
"""

from random import *


encorebesoin=True
while encorebesoin==True:
    print('MENU')   
    print("1-Cryptage d'un texte  à partir d'une clé fournie [César]")
    print("2-Décryptage d'un texte à partir d'une clé fournie [César]")
    print("3-Décryptage d'un texte sans la clé [César]")
    print("4-Cryptage d'un texte en morse")
    print("5-Décryptage d'un texte en morse")
    print("6-Fin du programme")

    choix=int(input('Quel est votre choix ?'))  


    if choix==1:
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   
        for x in range(len(alphabet)):
            alphabet.append(alphabet[x])
            
        texte=str(input('Quel est le texte a crypter ?'))   
        cle=int(input('Quel est la clé de cryptage ?'))   
        assert cle>=0 and cle<26,"La clé doit être valide(c'est à dire entre 0 et 25 inclus)"
        
        def cryptageLettre(lettre,alphabet,cle):   
            for i in range(len(alphabet)):
                if lettre==' ':
                    return ' '
                elif alphabet[i]==lettre:
                    return str(alphabet[i+cle])
            return lettre
        texteCrypte=str()

        for lettre in texte:
            lettre = lettre.upper()
            texteCrypte+=cryptageLettre(lettre,alphabet,cle)  
        
        print(texteCrypte)   
        
        
    if choix==2:
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   
        for x in range(len(alphabet)):
            alphabet.append(alphabet[x])
            
        texte=str(input('Quel est le texte a décrypter ?'))   
        cle=int(input('Quel est la clé de décryptage ?'))   
        assert cle>=0 and cle<26,"La clé doit être valide(c'est à dire entre 0 et 25 inclus)"   
        
        def decryptageLettre(lettre,alphabet,cle):   
            for i in range(len(alphabet)):
                if lettre==' ':   
                    return ' '
                elif alphabet[i]==lettre:
                    return str(alphabet[i-cle])
            return lettre
        texteDecrypte=str()

        for lettre in texte:
            lettre = lettre.upper()
            texteDecrypte+=decryptageLettre(lettre,alphabet,cle)   
        
        print(texteDecrypte)
        
        
    if choix==3:
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   #Définition de l'alphabet
        for x in range(len(alphabet)):
            alphabet.append(alphabet[x])
        
        cleA=1   #Définit la clé
        texte=str(input('Quel est le texte a décrypter ?'))
        
        def decryptageLettre(lettre,alphabet,cleA):   
            for i in range(len(alphabet)):
                if lettre==' ':   
                    return ' '
                if alphabet[i]==lettre: 
                    return str(alphabet[i-cleA])
            return lettre
            
        for i in range(25):
            
            texteDecrypte=str()
            for lettre in texte:
                lettre = lettre.upper()
                texteDecrypte+=decryptageLettre(lettre,alphabet,cleA)  
        
            print("Tentative de décryptage avec une clé de",cleA,":",texteDecrypte) 
            
            ressemblance=input("Si vous visualisez le texte en clair rentrer F (en majuscule ou minuscule) sinon entrée.") 
            assert ressemblance=='f' or ressemblance=='F' or ressemblance=='' or ressemblance==' ',"Veuillez rentrer une reponse valide" 
            if ressemblance=='f' or ressemblance=='F':   #Si la clé est la bonne
                print("Le texte décrypté :", texteDecrypte, "à été décrypté avec la clé de", cleA)  
                break 
            elif cleA==25:  
                print("Désolé, vous avez essayé toutes les valeurs de clé, le texte  a été  crypté selon une méthode non mono-alphabétique")
                break   
            elif ressemblance==' ' or ressemblance=='':  
                cleA+=1  
    if choix==4:
        alphabetMorse ={"A":' .-',"B":' -...',"C":' -.-.',"D":' -..',"E":' .',"F":' ..-.',"G":' --.',
                    "H":' ....',"I":' ..',"J":' .---',"K":' -.-',"L":' .-..',"M":' --',"N":' -.',
                    "O":' ---',"P":' .--.',"Q":' --.-',"R":' .-.',"S":' ...',"T":' -',"U":' ..-',
                    "V":' ...-',"W":' .--',"X":' -..-',"Y":' -.--',"Z":' --..'," ":"~"}
           
        texte=str(input('Quel est le texte a crypter ?'))  

        texteCryptéM=str()
        def cryptageLettreM(lettre,alphabetMorse):
            if lettre.isalpha():
                lettre=lettre.upper()
                lettre = alphabetMorse[lettre]
                return lettre
                
            elif lettre==' ':
                return ' ~ '
            

        for lettre in texte:  
            texteCryptéM+=cryptageLettreM(lettre,alphabetMorse)  
            
        
        print(texteCryptéM)
        
    if choix==5:
        alphabetinvers = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '~': ' '}                   
        texte=str(input('Quel est le texte a décrypter ?'))
        texteDecrypteM=str()
        texte=texte.split(' ')


        
        def decryptageMorse(symb,alphabetinvers):
            retour = alphabetinvers[symb]
            return retour

        for symb in texte:
            if symb!='':
                texteDecrypteM+=decryptageMorse(symb,alphabetinvers)
            else : 
                continue
        
        print(texteDecrypteM)
    if choix==6:
        print("Fin du programme") 
        encorebesoin=False
