#Challenge proposed at https://www.reddit.com/r/dailyprogrammer/comments/7qn07r/20180115_challenge_347_easy_how_long_has_the/
#Python3

moreLines = True;
enterTimes = []
exitTimes = []
print('Enter times below, each on a new line: ')
while moreLines :
    newLine = input()
    if newLine == '' :
        moreLines = False
    else :
        enterTimes.append(int(newLine.split()[0]))
        exitTimes.append(int(newLine.split()[1]))

firstIn = min(enterTimes)
lastOut = max(exitTimes)

timeSlots = [False] * (lastOut - firstIn)

for index, inTime in enumerate(enterTimes) :
    outTime = exitTimes[index]
    while inTime < outTime :
        timeSlots[inTime - firstIn] = True
        inTime += 1

print(sum(timeSlots))
