print("**********************************************")
word = ""
while len (word) < 6 or word.isalpha() == False:
	word = input("Please input a word longer than 5 letters.")
	if (len(word) < 6):
		print("Dude, I said less than 5 letters!")
print(word+ " is a seriously long word!")