class PrefixCode:
	def isOne(self, words):
		if len(words)==1:
			return "Yes"

		i = -1
		for ele1 in words:
			i+=1
			for ele2 in words:
				if len(ele2)> len(ele1):
					if ele2[:len(ele1)] == ele1:
						return "No, " + str(i)

		return "Yes"

test = PrefixCode()

print test.isOne(["10001", "011", "100", "001", "10"])
print test.isOne(["no", "nosy", "neighbors", "needed"])
print test.isOne(["1010", "11", "100", "0", "1011"])



