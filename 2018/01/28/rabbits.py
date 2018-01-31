#Solving problem for https://www.reddit.com/r/dailyprogrammer/comments/7s888w/20180122_challenge_348_easy_the_rabbit_problem/
#Written for Python2

def totalRabbits(males, females):
    total = 0
    total += sum(males)
    total += sum(females)
    return total

def advanceMonth(males, females):
    #rabbits reproduce if they are female and >= 4 months old
    num_reproducing = sum(females[4:])

    #add reproduced rabbits, this handles rabbits aging as well
    males.insert(0, num_reproducing * 5)
    females.insert(0, num_reproducing * 9)

    #rabbits die at 96 months
    num_killed = 0
    if len(males) > 96 :
        num_killed += males[96]
        males = males[:-1]
    if len(females) > 96 :
        num_killed += females[96]
        females = females[:-1]

    return num_killed

vals = map(int, raw_input("Enter [starting_males] [starting_females] [goal_number]: ").split())

males = [0, 0, vals[0]]
females = [0, 0, vals[1]]
goal_number = vals[2]

months_passed = 0
total_killed = 0

while totalRabbits(males, females) < goal_number :
    total_killed += advanceMonth(males, females)
    months_passed = months_passed + 1
    print(str(months_passed) + " months passed")
    print(str(totalRabbits(males, females)) + " rabbits")
    print("**********")

print("Months passed: " + str(months_passed))
print("Rabbits killed: " + str(total_killed))
