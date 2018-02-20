#Problem from https://www.interviewcake.com/question/python/single-riffle-check
# Given a full-deck (1-52) of cards and two half-decks, determine if the full
#  deck is a single-riffle shuffle of the two half-decks
import random

def checkForSingleRiffle(fullDeck, half1, half2) :
    half1Index = 0
    half2Index = 0
    for card in fullDeck :
        if half1Index < len(half1) and card == half1[half1Index] :
            half1Index += 1
        elif half2Index < len(half2) and card == half2[half2Index] :
            half2Index += 1
        else :
            return False

    return True

#TESTS
fullDeck = [x for x in range(1, 53)]
half1 = [x for x in range (1, 27)]
half2 = [x for x in range (27, 53)]
print(checkForSingleRiffle(fullDeck, half1, half2)) #expect True

random.shuffle(fullDeck)
half1 = fullDeck[0:26]
half2 = fullDeck[26:]

print(checkForSingleRiffle(fullDeck, half1, half2)) #expect True

half1 = []
half2 = []
for card in fullDeck :
    if len(half1) < len(half2) :
        half1.append(card)
    else:
        half2.append(card)

print(checkForSingleRiffle(fullDeck, half1, half2)) #expect True

temp = half1[20]
half1[20] = half2[10]
half2[10] = temp
print(checkForSingleRiffle(fullDeck, half1, half2)) #expect False
