class GuessTheNumber:
	def noGuesses(self, upper, answer):
		i = 0
		guess = 0
		lower = 1
		upper2 = upper
		while guess!= answer:
			print guess
			i+=1
			guess = (lower+upper2)/2
			if guess== answer:
				return i
			elif guess < answer:
				lower = guess+1
			elif guess > answer:
				upper2 = guess-1
			else:
				return None





test = GuessTheNumber()

print test.noGuesses(1000,750)






