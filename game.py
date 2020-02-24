import win_check
import pygame

pygame.init()

window_width = 500
window_height = 400
board_width = 80
board_height = 70
board_color = (150, 150, 150)
button_color = (175, 175, 175)
button_color_mouse_over = (195, 195, 195)

window = pygame.display.set_mode((window_width, window_height))
window.fill(board_color)
pygame.display.set_caption("Connect 4")

run = True
menu = True
how_to = False
end_screen = False
user = "User1"

board = pygame.image.load('board.jpg')
arrow = pygame.image.load('downwards_arrow.png')


def make_board():
	window.blit(board, (board_width, board_height))


def text_objects(text, font):
	text_surface = font.render(text, True, (0, 0, 0))
	return text_surface, text_surface.get_rect()


def menu_buttons():
	small_text = pygame.font.Font("freesansbold.ttf", 20)
	text_surf, text_rect = text_objects("Start game", small_text)
	text_rect.center = ((150+(200/2)), (50+(100/2)))
	window.blit(text_surf, text_rect)

	text_surf, text_rect = text_objects("How to play", small_text)
	text_rect.center = ((150+(200/2)), (150+(100/2)))
	window.blit(text_surf, text_rect)

	text_surf, text_rect = text_objects("Stats", small_text)
	text_rect.center = ((150+(200/2)), (250+(100/2)))
	window.blit(text_surf, text_rect)


def how_to_play():
	small_text = pygame.font.Font("freesansbold.ttf", 20)
	text1 = "Click on the arrows on top"
	text2 = "of each column to place a coin"
	text3 = "in that column. The goal of the"
	text4 = "game is to get four coins in a row."
	text5 = "Good luck!"
	text_surf, text_rect = text_objects(text1, small_text)
	text_rect.center = (250, 50)
	window.blit(text_surf, text_rect)
	text_surf, text_rect = text_objects(text2, small_text)
	text_rect.center = (250, 100)
	window.blit(text_surf, text_rect)
	text_surf, text_rect = text_objects(text3, small_text)
	text_rect.center = (250, 150)
	window.blit(text_surf, text_rect)
	text_surf, text_rect = text_objects(text4, small_text)
	text_rect.center = (250, 200)
	window.blit(text_surf, text_rect)
	text_surf, text_rect = text_objects(text5, small_text)
	text_rect.center = (250, 250)
	window.blit(text_surf, text_rect)

	text_surf, text_rect = text_objects("Back", small_text)
	text_rect.center = (250, 350)
	window.blit(text_surf, text_rect)


def end_screen_page():
	small_text = pygame.font.Font("freesansbold.ttf", 20)
	if check != "It's a tie!":
		text_surf, text_rect = text_objects("Congratulations! ", small_text)
		text_rect.center = (250, 125)
		window.blit(text_surf, text_rect)

		text_surf, text_rect = text_objects(check, small_text)
		text_rect.center = (250, 175)
		window.blit(text_surf, text_rect)
	else:
		text_surf, text_rect = text_objects(check, small_text)
		text_rect.center = (250, 125)
		window.blit(text_surf, text_rect)

	text_surf, text_rect = text_objects("Back to Main menu", small_text)
	text_rect.center = (250, 350)
	window.blit(text_surf, text_rect)


if __name__ == '__main__':
	while menu or how_to or run:		# Default run settings, loops through to allow back options
		run = True
		menu = True
		how_to = False
		end_screen = False

		while menu:  	# Loop for main menu
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					menu = False
					how_to = False
					run = False
					end_screen = False

				mouse_pos = pygame.mouse.get_pos()

				menu_buttons()

				pygame.display.update()

				if 150 < mouse_pos[0] < 350 and 50 < mouse_pos[1] < 150:		# Start game button
					pygame.draw.rect(window, button_color_mouse_over, (150, 50, 200, 100))

					if event.type == pygame.MOUSEBUTTONDOWN:
						menu = False
				else:
					pygame.draw.rect(window, button_color, (150, 50, 200, 100))

				if 150 < mouse_pos[0] < 350 and 150 < mouse_pos[1] < 250:		# How to play button
					pygame.draw.rect(window, button_color_mouse_over, (150, 150, 200, 100))

					if event.type == pygame.MOUSEBUTTONDOWN:
						menu = False
						how_to = True
				else:
					pygame.draw.rect(window, button_color, (150, 150, 200, 100))

				if 150 < mouse_pos[0] < 350 and 250 < mouse_pos[1] < 350:		# Stats button
					pygame.draw.rect(window, button_color_mouse_over, (150, 250, 200, 100))

					if event.type == pygame.MOUSEBUTTONDOWN:
						menu = False
				else:
					pygame.draw.rect(window, button_color, (150, 250, 200, 100))

		while how_to:		# Loop for how-to-play screen
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					how_to = False
					menu = False
					run = False
					end_screen = False

				mouse_pos = pygame.mouse.get_pos()
				window.fill(board_color)

				if 200 < mouse_pos[0] < 300 and 325 < mouse_pos[1] < 375:		# Start game button
					pygame.draw.rect(window, button_color_mouse_over, (200, 325, 100, 50))

					if event.type == pygame.MOUSEBUTTONDOWN:
						how_to = False
						run = False
						menu = True
				else:
					pygame.draw.rect(window, button_color, (200, 325, 100, 50))

				how_to_play()
			pygame.display.update()
		window.fill(board_color)

		if not menu and run:
			win_check.coin.avail_pos, win_check.coin.user1_list, win_check.coin.user2_list = win_check.coin.reset_game()
			check = ""
			user = "User1"
			make_board()

		while run:		# Main run screen
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					menu = False
					how_to = False
					end_screen = False

				mouse_pos = pygame.mouse.get_pos()

				check = win_check.checker()
				if check == "It's a tie!":
					print(check)
					end_screen = True
					run = False

				if check == "Player 1 wins!":
					print(check)
					end_screen = True
					run = False

				if check == "Player 2 wins!":
					print(check)
					end_screen = True
					run = False

				for i in (
						80, 120, 160, 200, 240, 280, 320,
						360):  # Makes boxes above columns that can be clicked to place coins
					if i < mouse_pos[0] < i+40 and 20 < mouse_pos[1] < 70:
						pygame.draw.rect(window, (225, 225, 225), (i, 20, 40, 50))

						if event.type == pygame.MOUSEBUTTONDOWN:
							try:
								coin1 = win_check.coin.Coin(window, user, ((i/40)-2)).make_coin()
							except IndexError:
								print("This column is full!")

							if user == "User1":
								user = "User2"
							else:
								user = "User1"
					else:
						pygame.draw.rect(window, (255, 255, 255), (i, 20, 40, 50))

				for i in (51, 91, 131, 171, 211, 251, 291, 331):  # Makes arrows
					window.blit(arrow, (i, -10))

			pygame.display.update()

		while end_screen:		# Loops end screen
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					menu = False
					how_to = False
					end_screen = False

				mouse_pos = pygame.mouse.get_pos()
				window.fill(board_color)

				if 150 < mouse_pos[0] < 350 and 325 < mouse_pos[1] < 375:
					pygame.draw.rect(window, button_color_mouse_over, (150, 325, 200, 50))

					if event.type == pygame.MOUSEBUTTONDOWN:
						menu = True
						end_screen = False

				else:
					pygame.draw.rect(window, button_color, (150, 325, 200, 50))

				end_screen_page()
			pygame.display.update()
		window.fill(board_color)

	pygame.quit()
