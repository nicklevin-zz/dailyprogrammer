def CheckForWinner(piece, x, y) :
	winner = False
	count = 0
	nope = False
	tempX = x
	tempY = y
	#top-left to bottom-right
	while not nope :
		if board[tempX-1][tempY-1]

	#top to bottom

	#bottom-left to top-right

	#left to right
	


board = [['.' for x in range(7)] for y in range(6)]
numChar = {'a': 0 , 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}

gameOver = False
xRow = 0
oRow = 0
while not gameOver :
	newMove = input("Enter next move: ").lower().split()
	
	#add 1st player's move to board
	for i in reversed(range(6)) :
		if board[i][numChar[newMove[0]]] == '.' :
			board[i][numChar[newMove[0]]] = 'X'
			xRow = i
			break
	#add 2nd player's move to board
	for i in reversed(range(6)) :
		if board[i][numChar[newMove[1]]] == '.' :
			board[i][numChar[newMove[1]]] = 'O'
			oRow = i
			break
	
	#print board
	for i in range(6) :
		print(board[i])
	
	#check for winner
	

	
print('Winner is.... : ' + winner)


