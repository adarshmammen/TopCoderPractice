class YahtzeeScore:
	def maxPoints(self, toss):
		tempsum, finalsum = 0,0
		
		for ele in toss:
			for check in toss:
				if ele == check:
					tempsum+= ele


			if tempsum > finalsum:
				finalsum = tempsum
			
			tempsum = 0
		
		return finalsum


test = YahtzeeScore()

print test.maxPoints((2,2,3,5,4))