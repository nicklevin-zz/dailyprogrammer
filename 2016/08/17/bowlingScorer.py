scorecard = input('Enter bowling scorecard: ')
frames = scorecard.split()
spare = False
strike = False
runningScore = 0

for frame in frames :
    firstScore = 0
    secondScore = 0

    firstBall = frame[0]
    if firstBall == '-' :
        firstScore = 0
        runningScore += 0
        spare == False
        if strike == True :
            spare = True
        strike = False
    
    elif firstBall == 'X' :
        runningScore += 10
        if spare == True :
            runningScore += 10
            spare = False
        if strike == True :
            runningScore += 10
            spare = True #doublestrike
        strike = True
        if(len(frame) != 3) :
            continue
    else :
        firstScore = int(firstBall)
        if spare == True :
            runningScore += firstScore
            spare = False
        if strike == True :
            runningScore += firstScore
            spare = True
        strike = False
        runningScore += firstScore
    
    secondBall = frame[1]
    if secondBall == '-' :
        secondScore = 0
        runningScore += 0
        spare = False
        if strike == True :
            spare = True
            strike = False
    elif secondBall == 'X' :
        if spare == True :
            runningScore += 10
        runningScore += 10
                        
    elif secondBall == '/' :
        secondScore = 10 - firstScore
        if spare == True :
            runningScore += secondScore
        runningScore += secondScore
        spare = True
        
    else :
        secondScore = int(secondBall)
        if spare == True :
            runningScore += secondScore
        runningScore += secondScore
        spare = False
    
    if len(frame) == 3 :
        thirdBall = frame[2]
        if thirdBall == '-':
            runningScore += 0
        elif thirdBall == 'X' :
            runningScore += 10
        else :
            runningScore += int(thirdBall)
print(runningScore)
