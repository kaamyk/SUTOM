def check_user_try(user_word, lenght, answer):

	result = []

	for i in range(0,lenght):
		letter_in_word = 0

		for letter in answer:
			if user_word[i] == letter:
				letter_in_word = 1

		if user_word[i] == answer[i]:
			result.append("right")

		elif (letter_in_word == 1)  and (user_word[i] != answer[i]) :
			result.append("in_word")

		else :
			result.append("false")

		

	return result


def define_color(results):

	colors = []

	for result in results:
		if result == "right":
			colors.append("RED")

		if result == "in_word":
			colors.append("YELLOW")

		if result == "false":
			colors.append("NONE")

	return colors


def debugger(user_word, answer_lenght):
	print (user_word)
	print(answer_lenght)
	if len (user_word) == answer_lenght:
		return 0

	elif len(user_word) < answer_lenght:
		return 2

	elif len(user_word) > answer_lenght:
		return 3
	
	else:
		return 1


def winning_grid(lenght):
	grid = []

	for i in range(0,lenght):
		grid.append("RED")

	return grid

