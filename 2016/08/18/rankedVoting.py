import operator
line = input('Enter number of voters and candidates:\t')
numVoters = int(line.split()[0])
numCandidates = int(line.split()[1])
candidates = input('Enter the names of the ' + str(numCandidates) + ' candidates:\t').split()
tallies = {}
for candidate in candidates:
    tallies[candidate] = 0.0
votes = []
for i in range(numVoters) :
    votes.append([])
    for j in input('Enter ballot #' + str(i + 1) + ':\t').split() :
        votes[i].append(int(j))

winner = False

votingRound = 1

while not winner :
    print('Round ' + str(votingRound) + '\n----------')
    
    for vote in votes :
        tallies[candidates[vote.index(0)]] += float((1 / numVoters))

    sortedTallies = sorted(tallies.items(), key=operator.itemgetter(1))

    for (candidate, tally) in reversed(sortedTallies) :
        if tally > 0.5 :
            winner = True
            print('Winner is ' + candidate + ' with ' + '{0:.1f}'.format(float(100 * tally)) + '%')
        else :
            print(candidate, ':', '{0:.1f}'.format(float(100 * tally)) + '%', end=', ')
    
    loser = sortedTallies[0][0]
    if not winner :
        print(loser + ' Eliminated')
        del tallies[loser]
        loserIndex = candidates.index(loser)
        candidates.remove(loser)
        for vote in votes :
            for i in range(len(vote)) :
                if vote[i] > vote[loserIndex] :
                    vote[i] -= 1
            vote.pop(loserIndex)
            
    for candidate, tally in tallies.items() :
        tallies[candidate] = 0.0

    votingRound += 1
