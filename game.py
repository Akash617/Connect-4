from coin import *
from win_check import checker

pygame.init()

window_width = 500
window_height = 400
board_width = 80
board_height = 70

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Connect 4")

run = True
user = "User1"

board = pygame.image.load('board.jpg')
arrow = pygame.image.load('downwards_arrow.png')


def make_board():
	window.blit(board, (board_width, board_height))


if __name__ == '__main__':
	make_board()

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			mouse_pos = pygame.mouse.get_pos()

			win_check = checker()
			if win_check == "Tie":
				print("It's a tie!")
				run = False

			if win_check == "User1 wins":
				print("Player 1 wins!")
				run = False

			if win_check == "User2 wins":
				print("Player 2 wins!")
				run = False

			for i in (80, 120, 160, 200, 240, 280, 320, 360):		# Makes boxes above columns that can be clicked to place coins
				if i < mouse_pos[0] < i+40 and 30 < mouse_pos[1] < 70:
					pygame.draw.rect(window, (225, 225, 225), (i, 30, 40, 40))

					if event.type == pygame.MOUSEBUTTONDOWN:
						try:
							coin1 = Coin(window, user, ((i/40)-2)).make_coin()
						except IndexError:
							print("This column is full!")

						if user == "User1":
							user = "User2"
						else:
							user = "User1"
				else:
					pygame.draw.rect(window, (255, 255, 255), (i, 30, 40, 40))

			for i in (51, 91, 131, 171, 211, 251, 291, 331):		# Makes arrows
				window.blit(arrow, (i, -10))

		pygame.display.update()

	pygame.quit()
