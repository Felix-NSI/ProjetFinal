encorebesoin=True
while encorebesoin==True:
    print('MENU')      #Affichage du menu et ses propositions
    print("1-Cryptage d'un texte  � partir d'une cl� fournie")
    print("2-D�cryptage de texte � partir d'une cl� fournie")
    print("3-D�cryptage de texte sans la cl�")
    print("4-Fin du programme")

    choix=int(input('Quel est votre choix ?'))   #Demande le choix de l'utilisateur par rapport au menu
    assert type(choix)==int,'Le nombre doit �tre entier'   #Contrainte pour que le choix soit un nombre entier
    assert choix<=4 and choix>=1,'Veuillez choisir une des 4 possibilit�'   #Contrainte pour que le choix soit compris dans les propositions du menu

    if choix==1:   #Si le choix est le premier
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   #D�finition de l'alphabet
        for x in range(len(alphabet)):   #D�double la liste
            alphabet.append(alphabet[x])
            
        texte=str(input('Quel est le texte a crypter ?'))   #Demande le texte � crypter
        cl�=int(input('Quel est la cl� de cryptage ?'))   #Demande la cl� de cryptage
        assert cl�>=0 and cl�<26,"La cl� doit �tre valide(c'est � dire entre 0 et 25 inclus)"   #Contrainte pour que la cl� soit valide
        
        def cryptageLettre(lettre,alphabet,cl�):   #D�finition du code de cryptage
            for i in range(len(alphabet)):
                if lettre==' ':   #au cas ou il y a un espace
                    return ' '
                elif alphabet[i]==lettre:   #d�tecte la lettre � crypter
                    return str(alphabet[i+cl�])
            return '@'  #en cas de caract�re inconnu
        texteCrypt�=str()

        for lettre in texte:   #Balaye les lettres de la phrase � crypter
            texteCrypt�+=cryptageLettre(lettre,alphabet,cl�)   #Remplacement des lettres par les lettres crypt�es
        
        print(texteCrypt�)   #Affiche le texte crypt�e
        
        
    if choix==2:   #Si le choix est le deuxi�me
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   #D�finition de l'alphabet
        for x in range(len(alphabet)):    #D�double la liste
            alphabet.append(alphabet[x])
            
        texte=str(input('Quel est le texte a d�crypter ?'))   #Demande le texte � d�crypter
        cl�=int(input('Quel est la cl� de d�cryptage ?'))   #Demande la cl� de d�cryptage
        assert cl�>=0 and cl�<26,"La cl� doit �tre valide(c'est � dire entre 0 et 25 inclus)"   #Contrainte pour que la cl� soit valide
        
        def decryptageLettre(lettre,alphabet,cl�):   #D�finition du code de d�cryptage
            for i in range(len(alphabet)):
                if lettre==' ':   #au cas ou il y a un espace
                    return ' '
                elif alphabet[i]==lettre:   #D�tecte la lettre � d�crypter
                    return str(alphabet[i-cl�])
            return '@'  #en cas de caract�re inconnu
        texteD�crypt�=str()

        for lettre in texte:   #Balaye les lettres de la phrase � d�crypter
            texteD�crypt�+=decryptageLettre(lettre,alphabet,cl�)    #Remplacement des lettres par les lettres d�crypt�es
        
        print(texteD�crypt�)   #Affiche le texte crypt�e
        
        
    if choix==3:   #Si le choix est le troisi�me
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   #D�finition de l'alphabet
        for x in range(len(alphabet)):    #D�double la liste
            alphabet.append(alphabet[x])
        
        cleA=1   #D�finit la cl�
        texte=str(input('Quel est le texte a d�crypter ?'))   #Demande le texte � d�crypter
        
        def decryptageLettre(lettre,alphabet,cleA):   #Red�finit le programme de d�cryptage 
            for i in range(len(alphabet)):
                if lettre==' ':   #au cas ou il y a un espace
                    return ' '
                if alphabet[i]==lettre:   #D�tecte la lettre � d�crypter
                    return str(alphabet[i-cleA])
            return '@'  #en cas de caract�re inconnu
            
        for i in range(25):
            
            texteDecrypte=str()
            for lettre in texte:   #Balaye les lettres de la phrase � d�crypter
                texteDecrypte+=decryptageLettre(lettre,alphabet,cleA)   #Remplacement des lettres par les lettres d�crypt�es
        
            print("Tentative de d�cryptage avec une cl� de",cleA,":",texteDecrypte)   #Affiche le texte d�crypt� avec le cl� utilis�e
            
            ressemblance=input("Si vous visualisez le texte en clair rentrer F (en majuscule ou minuscule) sinon entr�e")   #D�finit ressemblance
            assert ressemblance=='f' or ressemblance=='F' or ressemblance=='' or ressemblance==' ',"Veuillez rentrer une reponse valide"   #Contrainte pour que la r�ponse soit valide
            if ressemblance=='f' or ressemblance=='F':   #Si la cl� est la bonne
                print("Le texte d�crypt� :", texteDecrypte, "� �t� d�crypt� avec la cl� de", cleA)   #Affiche le texte d�crypt� et la cl� � utiliser 
                break   #Stop la boucle
            elif cleA==25:   #Si toutes les cl�s possible ont �t� utilis�es
                print("D�sol�, vous avez essay� toutes les valeurs de cl�, le texte  a �t�  crypt� selon une m�thode non mono-alphab�tique")
                break   #Stop la boucle
            elif ressemblance==' ' or ressemblance=='':   #Si la cl� n'est pas bonne
                cleA+=1   #Passe � la prochaine cl�
                
    if choix==4:   #Si le choix est le quatri�me
        print("Fin du programme")   #Affiche que c'est la fin du programme
        encorebesoin=False
