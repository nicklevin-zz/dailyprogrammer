#Check a string and determine if it has all unique characters

def checkForUniqueCharsSort(str) :
    str = ''.join(sorted(str))
    for i in range(1, len(str)) :
        if str[i] == str[i-1]:
            return False
    return True

def checkForUniqueCharsHash(str) :
    charsSeen = {}
    for i in range(0, len(str)):
        if str[i] in charsSeen :
            return False
        else :
            charsSeen[str[i]] = True
    return True

def checkForUniqueCharsBool(str) :
    charSeen = [False for x in range(128)]
    for char in str :
        if charSeen[ord(char)] :
            return False
        else :
            charSeen[ord(char)] = True
    return True

checkStrings = ["This should fail", "abcdefghijklmnopqrstuvwxyz", "ThisSHouldnOtFaIL"]
print("----------")

for checkString in checkStrings :
    print(checkString)
    print(checkForUniqueCharsHash(checkString))
    print(checkForUniqueCharsSort(checkString))
    print(checkForUniqueCharsBool(checkString))
    print("----------")
