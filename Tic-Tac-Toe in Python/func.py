import os
import random

def getplayernames():
# Gets Player A & B names
	while True:
		pa = str(input('Player A -> ')) # Player A
		pb = str(input('Player B -> ')) # Player B
		if pa != '' and pb != '' and pa != pb:
			break
		print("Put two different names! Try again.")
	return pa, pb
	
def randomplayer(pa, pb):
# Switches Player A & B randomly
	n = random.choice([0, 1])
	print(n)
	if n == 1:
		pa, pb = pb, pa
	return pa, pb

def cls():
# Clear screen (compatible on Windows & Linux)
# Source: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')

def draw(board, k, pa, pb, margin, spaces):
# Draw the board

	# Tutorial
	print('To put an X or an O, you must type in the xy coordinates.')
	print('x is the letter and y the number. (example: a0)')

	# Counter variables
	o = 97 # Columns
	
	# Board header
	print()
	print('{} vs {}'.format(pa, pb))
	print()
	
	# Draw board column letters
	print('{}  '.format(margin), end='')
	for i in range(k):
		print('{}{}'.format(chr(o), spaces), end='')
		o += 1
	
	# Draw Tic-Tac-Toe board
	for x in range(k):
		print()
		print('{}{} '.format(margin, x), end='')
		for y in range(k):
			print('{}{}'.format(board[x][y], spaces), end='')
		print()
	print()
	
def valid(move, k):
# Check if the Tic-Tac-Toe move input is valid
	if len(move) != 2:
		return False
	if move[0].isalpha():
		move0 = ord(move[0].lower()) - 97
	else:
		return False
	if move0 < 0 or move0 > k:
		return False
	try:
		move1 = int(move[1])
	except ValueError:
		return False
	if move1 < 0 or move1 >= k:
		return False
	return True
	
def CheckVictory(board, x, y):
# Check if victory parameters are met for a 3x3 tic-tac-toe board
# Source: https://codereview.stackexchange.com/questions/24764/tic-tac-toe-victory-check

    #check if previous move caused a win on vertical line 
    if board[0][y] == board[1][y] == board [2][y]:
        return True

    #check if previous move caused a win on horizontal line 
    if board[x][0] == board[x][1] == board [x][2]:
        return True

    #check if previous move was on the main diagonal and caused a win
    if x == y and board[0][0] == board[1][1] == board [2][2]:
        return True

    #check if previous move was on the secondary diagonal and caused a win
    if x + y == 2 and board[0][2] == board[1][1] == board [2][0]:
        return True

    return False

def CheckTie(board, k):
# Check if the board is tied
	for x in range(k):
		for y in range(k):
			if board[x][y] == '*':
				return False
	return True