from itertools import *

letterList = ['e','t','a','n']
letterListtwo = letterList+letterList

count=0

final = list((permutations(letterListtwo,8)))

for each in final:
    print(each)
    count+=1
print(count)
