#Answer to challenge listed at https://www.reddit.com/r/dailyprogrammer/comments/7ttiq5/20180129_challenge_349_easy_change_calculator/
#Python3
#brute force solution that generates all possible combinations of coins and checks their sum

import itertools

inputs = list(map(int, input("Enter the total followed by list of coins: ").split()))

totalNeeded = inputs[0]
coins = inputs[1:]

#sort coins high to low
coins.sort(reverse=True)

if sum(coins) > totalNeeded :   #sanity check
    allCombos = []
    for i in range(len(coins)) :
        for combo in list(map(list, itertools.combinations(coins, i))) :
            allCombos.append(combo)
    allCombos.sort(key=len)

    for combo in allCombos :
        if sum(combo) == totalNeeded :
            print(str(len(combo)) + ' coins used')
            print('Coins = ', end='')
            for coin in combo :
                print(str(coin), end=' ')
            print()
            exit()

print('No combination found, change cannot be made')
