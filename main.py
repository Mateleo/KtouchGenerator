file = open("liste_francais.txt", "r", encoding="UTF-8")

letterList = ['v','o','t']
accentE = ['é','è','ê']
final = []

def accentRemover(char):
    if char in accentE:
        return "e"
    elif char=="à":
        return "a"
    else:
        return char

def nameFinder(mylist):
    for word in mylist:
        if len(word)==5:
            return word
            break


def export(mylist,factor):
    if factor==0:
        factor = 100000
    count=0
    listCount=0
    name = nameFinder(mylist)
    f = open(name+'.txt',"w+")
    for i in mylist:
        listCount+=1
        if not(listCount%factor==0):
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
            tempL = accentRemover(letter)
            newWord = newWord+tempL
        if(len(newWord)>=5):
            final.append(newWord[:-1])
        print(word[:-1])
file.close()
print("---")
final = sorted(final, key=len)
final.reverse()
print(final)
export(final,0)
print(nameFinder(final))
