encorebesoin=True
while encorebesoin==True:
    print('MENU')      #Affichage du menu et ses propositions
    print("1-Cryptage d'un texte  à partir d'une clé fournie")
    print("2-Décryptage de texte à partir d'une clé fournie")
    print("3-Décryptage de texte sans la clé")
    print("4-Fin du programme")

    choix=int(input('Quel est votre choix ?'))   #Demande le choix de l'utilisateur par rapport au menu
    assert type(choix)==int,'Le nombre doit être entier'   #Contrainte pour que le choix soit un nombre entier
    assert choix<=4 and choix>=1,'Veuillez choisir une des 4 possibilité'   #Contrainte pour que le choix soit compris dans les propositions du menu

    if choix==1:   #Si le choix est le premier
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   #Définition de l'alphabet
        for x in range(len(alphabet)):   #Dédouble la liste
            alphabet.append(alphabet[x])
            
        texte=str(input('Quel est le texte a crypter ?'))   #Demande le texte à crypter
        clé=int(input('Quel est la clé de cryptage ?'))   #Demande la clé de cryptage
        assert clé>=0 and clé<26,"La clé doit être valide(c'est à dire entre 0 et 25 inclus)"   #Contrainte pour que la clé soit valide
        
        def cryptageLettre(lettre,alphabet,clé):   #Définition du code de cryptage
            for i in range(len(alphabet)):
                if lettre==' ':   #au cas ou il y a un espace
                    return ' '
                elif alphabet[i]==lettre:   #détecte la lettre à crypter
                    return str(alphabet[i+clé])
            return '@'  #en cas de caractère inconnu
        texteCrypté=str()

        for lettre in texte:   #Balaye les lettres de la phrase à crypter
            texteCrypté+=cryptageLettre(lettre,alphabet,clé)   #Remplacement des lettres par les lettres cryptées
        
        print(texteCrypté)   #Affiche le texte cryptée
        
        
    if choix==2:   #Si le choix est le deuxième
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   #Définition de l'alphabet
        for x in range(len(alphabet)):    #Dédouble la liste
            alphabet.append(alphabet[x])
            
        texte=str(input('Quel est le texte a décrypter ?'))   #Demande le texte à décrypter
        clé=int(input('Quel est la clé de décryptage ?'))   #Demande la clé de décryptage
        assert clé>=0 and clé<26,"La clé doit être valide(c'est à dire entre 0 et 25 inclus)"   #Contrainte pour que la clé soit valide
        
        def decryptageLettre(lettre,alphabet,clé):   #Définition du code de décryptage
            for i in range(len(alphabet)):
                if lettre==' ':   #au cas ou il y a un espace
                    return ' '
                elif alphabet[i]==lettre:   #Détecte la lettre à décrypter
                    return str(alphabet[i-clé])
            return '@'  #en cas de caractère inconnu
        texteDécrypté=str()

        for lettre in texte:   #Balaye les lettres de la phrase à décrypter
            texteDécrypté+=decryptageLettre(lettre,alphabet,clé)    #Remplacement des lettres par les lettres décryptées
        
        print(texteDécrypté)   #Affiche le texte cryptée
        
        
    if choix==3:   #Si le choix est le troisième
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   #Définition de l'alphabet
        for x in range(len(alphabet)):    #Dédouble la liste
            alphabet.append(alphabet[x])
        
        cleA=1   #Définit la clé
        texte=str(input('Quel est le texte a décrypter ?'))   #Demande le texte à décrypter
        
        def decryptageLettre(lettre,alphabet,cleA):   #Redéfinit le programme de décryptage 
            for i in range(len(alphabet)):
                if lettre==' ':   #au cas ou il y a un espace
                    return ' '
                if alphabet[i]==lettre:   #Détecte la lettre à décrypter
                    return str(alphabet[i-cleA])
            return '@'  #en cas de caractère inconnu
            
        for i in range(25):
            
            texteDecrypte=str()
            for lettre in texte:   #Balaye les lettres de la phrase à décrypter
                texteDecrypte+=decryptageLettre(lettre,alphabet,cleA)   #Remplacement des lettres par les lettres décryptées
        
            print("Tentative de décryptage avec une clé de",cleA,":",texteDecrypte)   #Affiche le texte décrypté avec le clé utilisée
            
            ressemblance=input("Si vous visualisez le texte en clair rentrer F (en majuscule ou minuscule) sinon entrée")   #Définit ressemblance
            assert ressemblance=='f' or ressemblance=='F' or ressemblance=='' or ressemblance==' ',"Veuillez rentrer une reponse valide"   #Contrainte pour que la réponse soit valide
            if ressemblance=='f' or ressemblance=='F':   #Si la clé est la bonne
                print("Le texte décrypté :", texteDecrypte, "à été décrypté avec la clé de", cleA)   #Affiche le texte décrypté et la clé à utiliser 
                break   #Stop la boucle
            elif cleA==25:   #Si toutes les clés possible ont été utilisées
                print("Désolé, vous avez essayé toutes les valeurs de clé, le texte  a été  crypté selon une méthode non mono-alphabétique")
                break   #Stop la boucle
            elif ressemblance==' ' or ressemblance=='':   #Si la clé n'est pas bonne
                cleA+=1   #Passe à la prochaine clé
                
    if choix==4:   #Si le choix est le quatrième
        print("Fin du programme")   #Affiche que c'est la fin du programme
        encorebesoin=False
