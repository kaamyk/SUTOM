from functions import check_user_try, define_color, debugger, winning_grid
from interface import send_text
secret_word = "bateau"
secret_word_in_array = []

win = 0

all_tries = []


def sutom_app():
	#Management of the answer
	for letter in secret_word :
		secret_word_in_array.append(letter)

	for i in range(0, 6):
		user_try = []
		#Managment of the user's try
		for user_letter in send_text() : #input("Votre proposition:")
			user_try.append(user_letter)

		#Check the user's try
		if debugger(user_try, len(secret_word)) == 0:
			all_tries.append(user_try)
			if (define_color(check_user_try(user_try, len(secret_word), secret_word_in_array)) != winning_grid(len(secret_word))) and (i < 6) :
				print (define_color(check_user_try(user_try, len(secret_word), secret_word_in_array)))

			if (define_color(check_user_try(user_try, len(secret_word), secret_word_in_array)) == winning_grid(len(secret_word))) and (i <= 6):
				all_tries.append(user_try)
				win = 1
				print (define_color(check_user_try(user_try, len(secret_word), secret_word_in_array))), win

			if (define_color(check_user_try(user_try, len(secret_word), secret_word_in_array)) != winning_grid(len(secret_word))) and (i > 6) :
				print ("You loose")

		elif debugger(user_try, len(secret_word)) == 2:
			print("Your porposition is to short")

		elif debugger(user_try, len(secret_word)) == 3:
			print("Your proposition is to long")

		else :
			print("Error")

sutom_app()