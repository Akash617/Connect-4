from coin import *


def checker():
	if not avail_pos[0] and not avail_pos[1] \
		and not avail_pos[2] and not avail_pos[3] \
		and not avail_pos[4] and not avail_pos[5] \
		and not avail_pos[6] and not avail_pos[7]:
		return "It's a tie!"

	for i in range(5):		# Checks all horizontal win conditions
		for j in range(7, -1, -1):

			if (i, j) in user1_list and (i+1, j) in user1_list\
				and (i+2, j) in user1_list and (i+3, j) in user1_list:
				return "Player 1 wins!"

			if (i, j) in user2_list and (i+1, j) in user2_list\
				and (i+2, j) in user2_list and (i+3, j) in user2_list:
				return "Player 2 wins!"

	for i in range(7):		# Checks all vertical win conditions
		for j in range(7, 2, -1):

			if (i, j) in user1_list and (i, j-1) in user1_list \
				and (i, j-2) in user1_list and (i, j-3) in user1_list:
				return "Player 1 wins!"

			if (i, j) in user2_list and (i, j-1) in user2_list \
				and (i, j-2) in user2_list and (i, j-3) in user2_list:
				return "Player 2 wins!"

	for i in range(5):		# Checks all upward diagonal win conditions
		for j in range(7, 2, -1):

			if (i, j) in user1_list and (i+1, j-1) in user1_list \
				and (i+2, j-2) in user1_list and (i+3, j-3) in user1_list:
				return "Player 1 wins!"

			if (i, j) in user2_list and (i+1, j-1) in user2_list \
				and (i+2, j-2) in user2_list and (i+3, j-3) in user2_list:
				return "Player 2 wins!"

	for i in range(5):		# Checks all downward diagonal win conditions
		for j in range(5):

			if (i, j) in user1_list and (i+1, j+1) in user1_list \
				and (i+2, j+2) in user1_list and (i+3, j+3) in user1_list:
				return "Player 1 wins!"

			if (i, j) in user2_list and (i+1, j+1) in user2_list \
				and (i+2, j+2) in user2_list and (i+3, j+3) in user2_list:
				return "Player 2 wins!"
