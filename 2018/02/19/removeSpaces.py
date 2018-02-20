#super simple problem - remove all spaces from the input strings
numInputsLeft = int(input())
while numInputsLeft > 0 :
    print(input().replace(' ', ''))
    numInputsLeft -= 1
