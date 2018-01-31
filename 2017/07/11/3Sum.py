#From https://www.reddit.com/r/dailyprogrammer/comments/6melen/20170710_challenge_323_easy_3sum/
#Enter a list of integers (including negatives) and find all sets of 3 of the numbers that sum to 0

originalNums = list(map(int, raw_input("Enter numbers:").split(' ')))

nums2 =[]
nums3 =[]

winners = set()

for num1 in originalNums :
    nums2 = list(originalNums)
    nums2.remove(num1)
    for num2 in nums2 :
        nums3 = list(nums2)
        nums3.remove(num2)
        for num3 in nums3 :
            if (num1 + num2 + num3) == 0 :
                winners.add(frozenset([num1, num2,num3]))

for winner in winners :
    winnerList = list(winner)
    print winnerList
