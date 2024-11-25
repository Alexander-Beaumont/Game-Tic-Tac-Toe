



class Gamelogic():
	
	@staticmethod
	def check_winner(board, symbol):
		for row in board.grid:
			if all(cell == symbol for cell in row):
				return 1
		for col in range(3):
			if all([board.grid[row][col] == symbol for row in range(3)]):
				return 1
		
		if all(board.grid[i][i] == symbol for i in range(3)) or all(board.grid[i][2-i] == symbol for i in range(3)):
			print(board.grid)
			return 1
		else:
			return 0



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
