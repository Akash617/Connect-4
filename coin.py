import pygame

avail_pos = [
		[(100, 90), (100, 130), (100, 170), (100, 210), (100, 250), (100, 290), (100, 330), (100, 370)],
		[(140, 90), (140, 130), (140, 170), (140, 210), (140, 250), (140, 290), (140, 330), (140, 370)],
		[(180, 90), (180, 130), (180, 170), (180, 210), (180, 250), (180, 290), (180, 330), (180, 370)],
		[(220, 90), (220, 130), (220, 170), (220, 210), (220, 250), (220, 290), (220, 330), (220, 370)],
		[(260, 90), (260, 130), (260, 170), (260, 210), (260, 250), (260, 290), (260, 330), (260, 370)],
		[(300, 90), (300, 130), (300, 170), (300, 210), (300, 250), (300, 290), (300, 330), (300, 370)],
		[(340, 90), (340, 130), (340, 170), (340, 210), (340, 250), (340, 290), (340, 330), (340, 370)],
		[(380, 90), (380, 130), (380, 170), (380, 210), (380, 250), (380, 290), (380, 330), (380, 370)]
		]

user1_list = []
user2_list = []


class Coin:
	def __init__(self, window, tag, column):
		self.radius = 18
		self.window = window
		self.column = int(column)
		self.tag = tag

		if self.tag == "User1":
			self.color = (255, 255, 0)
		else:
			self.color = (255, 0, 0)

		self.pos = avail_pos[self.column][-1]

	def make_coin(self):
		# noinspection PyAttributeOutsideInit
		self.coin = pygame.draw.circle(self.window, self.color, self.pos, self.radius)

		if self.tag == "User1":
			user1_list.append((self.column, len(avail_pos[self.column])-1))
		else:
			user2_list.append((self.column, len(avail_pos[self.column])-1))

		avail_pos[self.column].pop()
