import pygame
from player import Player
from board import Board
from gamelogic import Gamelogic

def main(args):
	
	board = Board()
	player1 = Player('player1', 'X')
	player2 = Player("player2", 'O')
	players = [player1, player2]
	
	current_player = 0
	pygame.init()
	screen = pygame.display.set_mode((600, 600))
	pygame.display.set_caption("Tic Tac Toe")
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:		
				running = False
				
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				x, y = event.pos
				col = (x // 200)
				row = (y // 200)
				print(f" y {row} x{col}")
				if board.grid[row][col] == None:
					board.grid[row][col] = players[current_player].symbol
					print(f"{players[current_player].name} has completed his turn")
	
			
	
		
				if Gamelogic.check_winner(board, players[current_player].symbol) == 1:
					print(f"{players[current_player].name}: Wins")
					running = False
				
				current_player = 1 - current_player
		
		board.display(screen)
	pygame.quit()	





if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
