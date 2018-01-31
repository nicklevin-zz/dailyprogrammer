import collections
while True :
    (word, anagram) = map(lambda x : x.replace(' ', ''), input().lower().replace('"', '').split('?'))
    if collections.Counter(word) == collections.Counter(anagram) :
        print("Is an anagram!")
    else :
        print("Not an anagram!")
