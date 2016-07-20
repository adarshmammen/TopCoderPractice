class FormatAmt:
	def amount(self, dollars, cents):
		li = list(str(dollars))
		print li
		result = []
		for i in range(len(li),0,-1):
			if i % 3 == 0 and i !=len(li) and i != 0:

				result.append(",")
			result.append(str(li[-i]))
	
		cent = str(cents)
		if len(cent) ==1:
			cent = "0" + str(cents)

		return "$" + "".join(result) + "." + cent



test = FormatAmt()

print test.amount(1000,1)