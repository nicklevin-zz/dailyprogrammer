#Challenge proposed @ https://www.reddit.com/r/dailyprogrammer/comments/7vx85p/20180207_challenge_350_intermediate_balancing_my/

transactions = list(map(int, input('Enter transactions: ').split()))

print(transactions)

preSum = [0] * (len(transactions) + 1)

for index in range(1, len(transactions) + 1) :
    preSum[index] = preSum[index-1] + transactions[index-1]

solutions = []
for index in range(len(transactions)) :
    if preSum[index] == preSum[len(transactions)] - preSum[index+1] :
        solutions.append(index)

print(solutions)
