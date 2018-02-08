#Taken from https://www.reddit.com/r/dailyprogrammer/comments/7vm223/20180206_challenge_350_easy_bookshelf_problem/
#As noted in comments, this problem is actually NP-hard, 

shelves = list(map(int, input("Enter shelf values: ").split()))
shelves.sort(reverse=True)

done = False
bookValues = [];

while not done :
    line = input('On each line enter book value followed by a space and book title: ')
    if line == '' :
        done = True
    else :
        bookValues.append(int(line.split()[0]))

bookValues.sort(reverse=True)

noSolution = False
shelvesUsed = set()

for book in bookValues :
    bookFits = False
    shelfIndex = 0
    while shelfIndex < len(bookValues) and bookFits == False :
        if book <= shelves[shelfIndex] :
            shelves[shelfIndex] -= book
            shelvesUsed.add(shelfIndex)
            bookFits = True
        else :
            shelfIndex += 1

    if bookFits == False :
        noSolution = True

if noSolution :
    print('No Solution!')
else :
    print(len(shelvesUsed))
