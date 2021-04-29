# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:12:38 2021

@author: Félix
"""

encorebesoinMorse=True
while encorebesoinMorse==True:
    print('MENU')    
    print("1-Cryptage en morse")
    print("2-Décryptage de Morse")
    print("3-Fin du programme")

    choix=int(input('Quel est votre choix ?'))   
    assert type(choix)==int,'Le nombre doit être entier'   
    assert choix<=3 and choix>=1,'Veuillez choisir une des 3 possibilité'  
    alphabetMorse ={"A":' .-',"B":' -...',"C":' -.-.',"D":' -..',"E":' .',"F":' ..-.',"G":' --.',
                    "H":' ....',"I":' ..',"J":' .---',"K":' -.-',"L":' .-..',"M":' --',"N":' -.',
                    "O":' ---',"P":' .--.',"Q":' --.-',"R":' .-.',"S":' ...',"T":' -',"U":' ..-',
                    "V":' ...-',"W":' .--',"X":' -..-',"Y":' -.--',"Z":' --..'," ":"~"}
    
    if choix==1:
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
            #print(cryptageLettreM(lettre,alphabetMorse))
        
        print(texteCryptéM)
        
    if choix==2:
        alphainvers = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '~': ' '}                   
        texte=str(input('Quel est le texte a décrypter ?'))
        texteDecrypteM=str()
        texte=texte.split(' ')
        print(texte)

        
        def decryptageMorse(symb,alphabetinvers):
            retour = alphainvers[symb]
            return retour

        for symb in texte:
            if symb!='':
                texteDecrypteM+=decryptageMorse(symb,alphabetMorse)
            else : 
                continue
        
        print(texteDecrypteM)
        
        

    if choix==3:
        print("Fin du programme")
        encorebesoinMorse=False
