file = open("bible/BiblePlain.txt", "r", encoding="UTF-8")
bible = file.read()

fileToWrite = open("BibleLignes.txt", "w", encoding="UTF-8")

letterList = ['e','o','t','u','r','a','n']

accentE = ['é','è','ê']
validList = letterList.append('\n')

def accentRemover(char):
    if char in accentE:
        return "e"
    elif char=="à":
        return "a"
    else:
        return char

for letter in range(0,len(bible)):
    if((ord(bible[letter])==32) and (ord(bible[letter-1])!=46)): #si espace et avant point ne pas écrire
        fileToWrite.write(bible[letter])
    elif(bible[letter]=="\n"): #si retour à la ligne mettre un espace
        fileToWrite.write(' ')
    elif((ord(bible[letter])>=65) and (ord(bible[letter])<=90)): #si majuscule
        if(ord(bible[letter-2])==46 or ord(bible[letter-4])==46): #si point avant faire un retour à la ligne
            fileToWrite.write("\n")
        fileToWrite.write(bible[letter])
    elif((ord(bible[letter])>=97 and ord(bible[letter])<=122) or (ord(bible[letter])==39) or (ord(bible[letter])==46) or (ord(bible[letter])>=224 and ord(bible[letter])<=255)): #lettre et tout le merdier
        fileToWrite.write(bible[letter])
        
fileToWrite.close()
