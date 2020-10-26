file = open("bible/BiblePlain.txt", "r", encoding="UTF-8")
bible = file.read()

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
    if(ord(bible[letter])>=65 and ord(bible[letter])<=90):
        print(bible[letter])
