from functions import check_user_try, define_color, debugger
secret_word = "bateau"

secret_word_lenght = len(secret_word)

user_try = []
playable_array = []

secret_word_in_array = []

#Management of the answer
for letter in secret_word :
	secret_word_in_array.append(letter)

print (secret_word_in_array)

#Managment of the user's try
for user_letter in input("Votre proposition :") :
	user_try.append(user_letter)
print (user_try)

#Check the user's try
if debugger(user_try, secret_word_lenght) == 0:

	print (define_color(check_user_try(user_try, secret_word_lenght, secret_word_in_array)))

elif debugger(user_try, secret_word_lenght) == 2:
	print("Your porposition is to short")

elif debugger(user_try, secret_word_lenght) == 3:
	print("Your proposition is to long")

else :
	print("Error")