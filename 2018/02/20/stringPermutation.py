#Determine if two strings passed in are permutations of each other
# Simple solution is to sort both strings and then check if they are equal

#Case sensitive and whitespace sensitive, assuming chars are all ASCII
def checkForPermutation(str1, str2):
    if len(str1) != len(str2) :
        return False

    charCounts = [0 for x in range(128)] #space for a->z
    for char in str1 :
        charCounts[ord(char)] += 1
    for char in str2 :
        charCounts[ord(char)] -= 1

    for count in charCounts :
        if count != 0 :
            return False

    return True


testStringPairs = [
    ['abcde  fgh', 'hgf edcb a'],
    ['bDDDfdsa', 'ddbdFDAS'],
    ['racecar', 'CARRACE'],
    ['abcd', 'abcddbca'],
    ['aAaa B', 'aaaB A'],
    ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'],
    ['abcdefghijklmnopqrstuvwxyz', 'zyxwvuttrqponmlkjihgfedcba']
]

for pair in testStringPairs :
    print(pair)
    print(checkForPermutation(pair[0], pair[1]))
