# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:58:53 2021

@author: Félix 
"""

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
    print("6-Cryptage avec le Projet R")
    print("7-Décryptage avec le projet R")
    print("8-Fin du programme")

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
                print("Désolé, vous avez essayé toutes les valeurs de clé, le texte  a été  crypté selon une méthode différente au code de César.")
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
        
        alphabetmin=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
    alphabetmaj=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if choix==6:

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

        
    if choix==7:
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

    if choix==8:
        print("Fin du programme") 
        encorebesoin=False
