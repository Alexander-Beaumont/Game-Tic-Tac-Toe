
EMPTY = '-'


class Player:
	
	def __init__(self, name, symbol):
		self.name = name
		self.symbol = symbol
	
	def make_move(self, board):
		result = input(f"{self.name} you are {self.symbol}'s Enter the row an column in the format row,col: ")
		y, x = result.split(',')
		x = int(x)
		y = int(y)
		if board.grid[y-1][x-1] == EMPTY:
			board.update(y-1,x-1, self.symbol)
		else:
			print("Invalid Move")


if __name__ == '__main__':
    import sys
    
    
    
    
    sys.exit(main(sys.argv))



"""
class Player:
	
	def __init__(self, name, symbol):
		self.name = name
		self.symbol = symbol
	
	def make_move(self, board):
		result = input("Enter the row an column in the format row,col: ")
		y, x = result.split(',')
		x = int(x)
		y = int(y)
		if board.grid[y-1][x-1] != self.symbol:
			board.grid[y-1][x-1] = self.symbol
		else:
			print("Invalid Move")


if __name__ == '__main__':
    import sys
    
    
    
    
    sys.exit(main(sys.argv))
"""
