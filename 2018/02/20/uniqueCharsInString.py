def checkForUniqueChars(str) :
    str = ''.join(sorted(str))
    for i in range(1, len(str)) :
        if str[i] == str[i-1]:
            print("False, '{0}' is repeated".format(str[i]))
            return False
    return True

if checkForUniqueChars(input()):
    print('All chars unique')
