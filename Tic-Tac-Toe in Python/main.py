from func import *


def main():

	# Tic-Tac-Toe board variables
	k = 3 # board size
	board = [['*' for _ in range(k)] for _ in range(k)]
	xo = 'X'
	check = True
	won = False
	tie = False

	# Draw function formatting
	margin = ' ' * 2
	spaces = ' ' * 2

	# Greetings
	print('Hello, welcome to Tic-Tac-Toe in python... What are you names?')
	pa, pb = getplayernames()
	pa, pb = randomplayer(pa, pb)
	cp = pa # Current Player
	cls()

	# Game
	while True:

		while True:
			# Clear screen
			cls()
			
			# Draw board
			draw(board, k, pa, pb, margin, spaces)
			if not check:
				print('Invalid Input, try again.')
				
			if won:
				print('{} has won!'.format(cp))
				break
			elif tie:
				print('Game is tied!')
				break
			
			# Player move
			move = input('[ {} ] ({}) -> '.format(cp, xo))
			check = valid(move, k)
			if check:
				movex = int(move[1])
				movey = ord(move[0]) - 97
			if check and board[movex][movey] == '*':
				break
			check = False
		
		if won or tie:
			break
		
		# Make changes to the board
		board[movex][movey] = xo
		
		# Check victory status
		won = CheckVictory(board, movex, movey)
		tie = CheckTie(board, k)
		
		# Player turn
		if not won and not tie:
			if cp == pa:
				cp = pb
				xo = 'O'
			else:
				cp = pa
				xo = 'X'


if __name__ == "__main__":
	main()
	
	# Prevent app from closing
	closeapp = 'r'
	while closeapp == 'r':
		closeapp = input('Press [Enter] to exit or [r] to restart: ')
		if closeapp == 'r':
			cls()
			main()
