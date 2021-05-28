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



        
            

        
def cryptageLettre(lettre,alphabet,cle):
    for i in range(len(alphabet)):
        if lettre==' ':
            return ' '
        elif alphabet[i]==lettre:
            return alphabet[i+cle]
    return lettre
def crypt1(texte,cle):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    texteCrypte=str()
    for lettre in texte:
        lettre = lettre.upper()
        texteCrypte+=cryptageLettre(lettre,alphabet,cle)  
        
    print(texteCrypte)   
        
def debut1():

    texte=str(input('Quel est le texte a crypter ?'))   
    cle=int(input('Quel est la clé de cryptage ?'))   
    
    crypt1(texte,cle)
#debut1()
            

def debut2():
            
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']            
    texte=str(input('Quel est le texte a décrypter ?'))
    cle=int(input('Quel est la clé de décryptage ?'))   
  
    texteDecrypte=str()
    for lettre in texte:
        lettre = lettre.upper()
        texteDecrypte+=decryptageLettre(lettre,alphabet,cle)   
    print(texteDecrypte)
def decryptageLettre(lettre,alphabet,cle):   
    for i in range(len(alphabet)):
        if lettre==' ':   
            return ' '
        elif alphabet[i]==lettre:
            return str(alphabet[i-cle])
    return lettre
#debut2()

def decryptageLettre(lettre,alphabet,cleA):   
    for i in range(len(alphabet)):
        if lettre==' ':   
            return ' '
        if alphabet[i]==lettre: 
            return str(alphabet[i-cleA])
    return lettre
def debut3():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cleA=1
    texte=str(input('Quel est le texte a décrypter ?'))
    for i in range(25):
        texteDecrypte=str()
        for lettre in texte:
            lettre = lettre.upper()
            texteDecrypte+=decryptageLettre(lettre,alphabet,cleA)
        print("Tentative de décryptage avec une clé de",cleA,":",texteDecrypte) 
            
        ressemblance=input("Si vous visualisez le texte en clair rentrer un caractère sinon entrée.") 
            
        if ressemblance.isalpha():
            print("Le texte décrypté :", texteDecrypte, "à été décrypté avec la clé de", cleA)  
            break 
        elif cleA==25:  
            print("Désolé, vous avez essayé toutes les valeurs de clé, le texte  a été  crypté selon une méthode différente au code de César.")
            break   
        elif ressemblance==' ' or ressemblance=='':  
            cleA+=1 
#debut3()

def debut4():
            
    alphabetMorse ={"A":' .-',"B":' -...',"C":' -.-.',"D":' -..',"E":' .',"F":' ..-.',"G":' --.',
                    "H":' ....',"I":' ..',"J":' .---',"K":' -.-',"L":' .-..',"M":' --',"N":' -.',
                    "O":' ---',"P":' .--.',"Q":' --.-',"R":' .-.',"S":' ...',"T":' -',"U":' ..-',
                    "V":' ...-',"W":' .--',"X":' -..-',"Y":' -.--',"Z":' --..'," ":"~"}
           
    texte=str(input('Quel est le texte a crypter ?'))  

    texteCryptéM=str()        
    for lettre in texte:  
        texteCryptéM+=cryptageLettreM(lettre,alphabetMorse)
    print(texteCryptéM)
def cryptageLettreM(lettre,alphabetMorse):
    if lettre.isalpha():
        lettre=lettre.upper()
        lettre = alphabetMorse[lettre]
        return lettre
                
    elif lettre==' ':
        return ' ~ '
#debut4()
        

def debut5():
            
    alphabetinvers = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '~': ' '}                   
    texte=str(input('Quel est le texte a décrypter ?'))
    texteDecrypteM=str()
    texte=texte.split(' ')
    for symb in texte:
        if symb!='':
            texteDecrypteM+=decryptageMorse(symb,alphabetinvers)
        else : 
            continue
        
    print(texteDecrypteM)


        
def decryptageMorse(symb,alphabetinvers):
    retour = alphabetinvers[symb]
    return retour


#debut5()

    
    

def debut6():
    alphabetmin=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
    alphabetmaj=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']            

    texte=str(input('Quel est le texte a crypter ?'))  
    texteCrypteR=str()
    print(cryptageR(texte,alphabetmin,alphabetmaj))
            
            
def defcleR(alphabetmin):
    cleR=''
    hasacle = randint(2,6)
    for i in range(hasacle):
        cleR += alphabetmin[randint(0,25)]
    return cleR
def cryptageR(texte,alphabetmin,alphabetmaj):
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
        
#debut6()

        
                
        

        

        



        

        
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
def debut7():
    
    texte=str(input('Quel est le texte a décrypter ?'))
    cleR = str(input("Quelle est la clé ?"))
    texteDecrypteR= decryptageR(texte,cleR)
    
    print(texteDecrypteR)
#debut7()


