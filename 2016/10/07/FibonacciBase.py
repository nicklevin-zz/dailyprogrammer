(base, num) = input().split(' ')
result = 0
i = 0
fib1 = 0
fib2 = 0

def getFibListUpTo(number) :
    i = 0
    fibList = []
    while i <= number :
        i = nextFib()
        fibList.append(i)
    del fibList[-1]
    return fibList

def nextFib() :
    global fib1, fib2
    if fib1 == 0 :
        fib1 = 1
        return fib1
    if fib1 > fib2 :
        fib2 = fib1 + fib2
        return fib2
    else :
        fib1 = fib1 + fib2
        return fib1

if base not in ('F', '10'):
    print("Enter 'F' or '10' followed by the number to convert")
    exit(0)

elif base == 'F' :
    num = list(num)
    num.reverse()
    for digit in num :
        i = nextFib()
        if digit == '1' :
            result += i

else :
    num = int(num)
    seq = getFibListUpTo(num)
    seq.reverse()
    result = ''
    for fib in seq :
        if fib <= num :
            result = result + '1'
            num -= fib
        else :
            result = result + '0'

print('Result: {}'.format(result))
