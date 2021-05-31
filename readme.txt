D3CR1PT0

I.	Description Générale
Le D3CR1PT0 est un projet dans le cadre du cours de Numérique et Sciences Informatiques en Première. D3CR1PT0 a pour but de crypter (Opération par laquelle un message est rendu inintelligible à quiconque ne possède pas la clé permettant de retrouver la forme initiale. Source : Google) et décrypter avec trois méthodes : le code de César, le Morse et le code du Projet R. Le tout regroupé dans une interface graphique réalisée par tkinter.
	Premièrement, Le code César est un chiffrement basé sur un décalage de l'alphabet (déplacement des lettres plus loin dans l'alphabet), il s'agit d'une substitution monoalphabétique, c'est-à-dire qu'une même lettre n'est remplacée que par une seule autre (toujours identique pour un même message). 
	Puis, Le code Morse international1, ou l’alphabet Morse international, est un code permettant de transmettre un texte à l’aide de séries d’impulsions courtes et longues, qu’elles soient produites par des signes, une lumière, un son ou un geste. Ici, les lettres seront représentées par des ‘’-‘’ (pour un signal long) et des ‘’.’’ (pour les courts). Les espaces seront représentés par un ‘’~’’.
	Pour finir, le Projet R, est un code de ma conception qui consiste à mettre aléatoirement des lettres minuscules les unes derrière les autres et insérer des majuscules, qu’il faut lire pour avoir le message. Pour complexifier un peu le code : il existe une clé composée de lettres minuscules. Si cette clé est devant une majuscule, il ne faut pas la lire.

II.	Présentation d’une partie du code

Une des parties fort intéressantes pour moi était le cryptage et décryptage dont voici le code :

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

Cette partie m’a donné du fil à retorde à cause des caractères multiples qu’il faut pour une seule lettre, ce qui fait que si l’on veut balayer le contenu du message pour le décrypter, il fallait diviser les lettres, ainsi, j’ai séparé à chaque espace (il y en a entre chaque lettre et mot). 


III.	Extensions possibles

L’une des extensions que j’aurais bien aimé ajouter au code aurait été le multi cryptage en unissant les différentes méthodes. Par exemple crypter un message avec le code de César, puis crypter ce rendu en Projet R pour finir avec le Morse. Seul problème : le morse ne peut faire de différence entre majuscules et minuscules, entravant ainsi le décryptage avec le Projet R.
