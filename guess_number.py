def main():
	print "Guess number between 1 and 100"
	random_number=40
	found=False

	while not found:
		number_guess=input("Enter your guess: ")
		if number_guess==random_number:
			print "Good!That's it"
			found= True
		else:
			print "That's not it"

if __name__=='__main__':
	main()
