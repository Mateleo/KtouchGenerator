file = open("liste_francais.txt", "r", encoding="UTF-8")

letterList = ['v','o','t','e']
accentE = ['é','è','ê']
final = []

def accentRemover(char):
    if char in accentE:
        return "e"
    elif char=="à":
        return "a"
    elif char=="ï":
        return "i"
    elif char=="ö":
        return "o"
    elif char=="ô":
        return "o"
    else:
        return char

def nameFinder(mylist):
    for word in mylist:
        if len(word)==5:
            return word
            breakd


def export(mylist,factor):
    factor = 100//factor
    factorCounter=1
    count=0
    listCount=0
    name = nameFinder(mylist)
    f = open('exos/'+name+'.txt',"w+")
    for i in mylist:
        listCount+=1
        if factorCounter==factor:
            count = count+len(i)+1
            if i==mylist[-1]:
                f.write(i)
            else:
                if((count+len(mylist[listCount]))>60):
                    f.write(i)
                    f.write("\n")
                    count=0
                elif count<60:
                    i = i+" "
                    f.write(i)
            factorCounter=1
        else:
            factorCounter+=1

validList = letterList.append('\n')

for word in file:
    breaker=1
    for letter in word:
        tempL = accentRemover(letter)
        if(tempL not in letterList):
            breaker=0
    if breaker!=0:
        newWord = ""
        for letter in word:
            tempL = letter
            newWord = newWord+tempL
        if(len(newWord)>3):
            final.append(newWord[:-1])
        print(word[:-1])
file.close()
print("---")
final = sorted(final, key=len)
final.reverse()
print(final)
export(final,100)
print(nameFinder(final))
