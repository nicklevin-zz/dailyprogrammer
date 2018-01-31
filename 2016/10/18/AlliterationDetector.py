stopWords = ['I','a','about','an','and','are','as','at','be','by','com','for','from',
             'how','in','is','it','of','on','or','that','the','this','to','was','what',
             'when','where','who','will','with','the']

import re

numLines = int(input())
lines = []
for line in range(numLines) :
    lines.append(re.sub('[,."]', '', input()).split(' '))

for line in lines :
    for word in line[:] :
        if word in stopWords :
            line.remove(word)
    print(lines)
    streak = 0
    startingChar = ''
    allitString = ''
    allitList = []
    for word in line :
        if word[0].lower() != startingChar :
            if streak >= 2 :
                allitList.append(allitString)
            streak = 1
            startingChar = word[0].lower()
            allitString = word
        else :
            streak += 1
            allitString += ' ' + word
    if streak >= 2 :
        allitList.append(allitString)
    for allit in allitList :
        print(allit, end='\t')
    print('')


