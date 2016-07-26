class FixedPointTheorem:
	def cycleRange(self, R):
		x = (0.25)
		count = 0
		for i in range(200000):
			x = R * x * (1 - x)
			count +=1
		max = (x)
		min = (x)
		while count < 201001:
			count+=1
			x = R * x * (1 - x)
			if x > max:
				max = x
			elif x < min:
				min = x
			else:
				continue
		return max - min






test = FixedPointTheorem()

print test.cycleRange(3.05)






