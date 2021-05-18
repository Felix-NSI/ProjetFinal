encorebesoin=True
while encorebesoin==True:
    print('MENU')   
    print("1-Cryptage d'un texte  � partir d'une cl� fournie")
    print("2-D�cryptage de texte � partir d'une cl� fournie")
    print("3-D�cryptage de texte sans la cl�")
    print("4-Fin du programme")

    choix=int(input('Quel est votre choix ?'))  
    assert type(choix)==int,'Le nombre doit �tre entier'  
    assert choix<=4 and choix>=1,'Veuillez choisir une des 4 possibilit�'

    if choix==1:
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   
        for x in range(len(alphabet)):
            alphabet.append(alphabet[x])
            
        texte=str(input('Quel est le texte a crypter ?'))   
        cle=int(input('Quel est la cl� de cryptage ?'))   
        assert cle>=0 and cle<26,"La cl� doit �tre valide(c'est � dire entre 0 et 25 inclus)"
        
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
            
        texte=str(input('Quel est le texte a d�crypter ?'))   
        cle=int(input('Quel est la cl� de d�cryptage ?'))   
        assert cle>=0 and cle<26,"La cl� doit �tre valide(c'est � dire entre 0 et 25 inclus)"   
        
        def decryptageLettre(lettre,alphabet,cle):   
            for i in range(len(alphabet)):
                if lettre==' ':   
                    return ' '
                elif alphabet[i]==lettre:
                    return str(alphabet[i-cle])
            return lettre
        texteDecrypte=str()

        for lettre in texte:  
            texteDecrypte+=decryptageLettre(lettre,alphabet,cle)   
        
        print(texteDecrypte)
        
        
    if choix==3:
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   #D�finition de l'alphabet
        for x in range(len(alphabet)):
            alphabet.append(alphabet[x])
        
        cleA=1   #D�finit la cl�
        texte=str(input('Quel est le texte a d�crypter ?'))
        
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
                texteDecrypte+=decryptageLettre(lettre,alphabet,cleA)  
        
            print("Tentative de d�cryptage avec une cl� de",cleA,":",texteDecrypte) 
            
            ressemblance=input("Si vous visualisez le texte en clair rentrer F (en majuscule ou minuscule) sinon entr�e") 
            assert ressemblance=='f' or ressemblance=='F' or ressemblance=='' or ressemblance==' ',"Veuillez rentrer une reponse valide" 
            if ressemblance=='f' or ressemblance=='F':   #Si la cl� est la bonne
                print("Le texte d�crypt� :", texteDecrypte, "� �t� d�crypt� avec la cl� de", cleA)  
                break 
            elif cleA==25:  
                print("D�sol�, vous avez essay� toutes les valeurs de cl�, le texte  a �t�  crypt� selon une m�thode non mono-alphab�tique")
                break   
            elif ressemblance==' ' or ressemblance=='':  
                cleA+=1  
                
    if choix==4:
        print("Fin du programme") 
        encorebesoin=False
