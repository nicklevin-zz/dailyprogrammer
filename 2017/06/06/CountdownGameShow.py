import itertools
import time

#From: https://www.reddit.com/r/dailyprogrammer/comments/6fe9cv/20170605_challenge_318_easy_countdown_game_show/
# Enter a list of whole numbers (separated by a space) and then finally a target number (all on one line)
# This program finds all the orders of numbers and operands that produce the target numbers
# ex. '4 5 2 12' => 5-2*4=12
# Note that order of operations is not followed in the output - proceeds right-to-left

opTranslate = { #not used, slower than if/else lookup (see below)
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    '*': lambda x,y: x*y,
    '/': lambda x,y: x/y
}

def testCombo(nums, ops, target) :
    #print('Testing ' + str(nums) + ' and ' + str(ops))
    runningValue = nums[0]
    for i, op in enumerate(ops) :

        #runningValue = opTranslate[op](runningValue, nums[i+1])

        if op == '+':   #using this op if/else is faster than using op-table lookup
            runningValue = runningValue + nums[i+1]
        elif op == '-':
            runningValue = runningValue - nums[i+1]
        elif op == '*':
            runningValue = runningValue * nums[i+1]
        elif op == '/':
            runningValue = runningValue / nums[i+1]

    if runningValue == target:
        return True
    else :
        return False

val = input()
startTime = time.time()
nums = val.split()
nums = list(map(int, nums))
target = nums.pop() #by default returns and discards last value in list

allOpCombos = list(itertools.product(['+','-','*','/'], repeat=len(nums)-1))

for numTuple in itertools.permutations(nums):
    numOrder = list(numTuple)
    for ops in allOpCombos :
        if testCombo(numOrder, ops, target) is True :
            for i, num in enumerate(numOrder):
                print(str(num), end='')
                if i < len(ops):
                    print(ops[i], end='')
            print('=' + str(target))
print('Took {0} seconds'.format(time.time() - startTime))
