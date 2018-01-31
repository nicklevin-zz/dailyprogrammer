
while(True) :
    number = int(input())
    i = 2
    factorial = False
    while(number > 0):
        number = number / i
        i += 1
        if number == i:
            factorial = True
            break
        if number < i :
            factorial = False
            break

    if factorial is True:
        print(str(int(number)) + '!')
    else :
        print("None!")

