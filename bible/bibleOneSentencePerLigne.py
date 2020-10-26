fileToRead = open("BiblePlain.txt", "r", encoding="UTF-8")
bible = fileToRead.read()
fileToRead.close()

fileToWrite = open("BiblePhraseLignes.txt", "w", encoding="UTF-8")



for letter in range(0,len(bible)):
var = ord(bible[letter])

    if (var <= 65 or var >=90) or (ord(bible[letter+1]) <= 65 or ord(bible[letter+1]) >=90)
        if(var<48 or var>57) and (var<127 or var>192)):
            if (var < 256 and var != 10):
                fileToWrite.write(bible[letter])
