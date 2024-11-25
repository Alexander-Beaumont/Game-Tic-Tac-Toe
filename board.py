import pygame


class Board:
	def __init__(self):
		self.grid = [[None for i in range(3)] for i in range(3)]

	def update(self, y, x, value):
		self.grid[y][x] = value
	
	def display_grid(self, screen):
		for col in range(1, 3):
			pygame.draw.line(screen, (0, 0, 0), (col*200, 0), (col*200, 600))
		for row in range(1, 3):
			pygame.draw.line(screen, (0,0,0), (0, row*200), (600, row*200))
		
	def display_pieces(self, screen):
		for row in range(3):
			for col in range(3):
				if self.grid[row][col] == 'O':
					pygame.draw.circle(screen, (0, 255, 255), (int(col*200+200*0.5), int(row*200 + 200*0.5)), 75, 10)
					
				elif self.grid[row][col] == 'X':	
					pygame.draw.line(screen, (0, 0, 255), (col * 200 + 40, row * 200 + 40), (col * 200 + 160, row * 200 + 160), 10)
					pygame.draw.line(screen, (0, 0, 255), (col * 200 + 40, row * 200 + 160), (col * 200 + 160, row * 200 + 40), 10)
	def display(self, screen):
		screen.fill((255,255,255))
		self.display_grid(screen)
		self.display_pieces(screen)
		pygame.display.flip()
						
		



#class Board:
#	def __init__(self):
#		self.grid = [['-' for i in range(3)] for i in range(3)]
	
#	def update(self, location, value):
#		pass
		
#	def display(self):
		
#		for i in self.grid:
#			print("|", end='')
#			for j in i:
#				print(j,end='')
#			print("|")
