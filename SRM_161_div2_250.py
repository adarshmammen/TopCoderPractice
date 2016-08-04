class CardCount:
	def dealHands(self, numPlayers, deck):
		n = numPlayers
		s = str(deck)
		ret = []
		output = [[] for z in range(n)]
		output2 = []
		output3 = []

		i = len(s) % n

		new_s = len(s) - i

		if new_s == 0:
			return [""]*n
		else:
			j = 0
			for ele in s[:new_s]:
				output[j].append(ele)
				j+=1
				j = j%n
			for i,ele in enumerate(output):
				output2.append(map(int,output[i]))
			for i,ele in enumerate(output2):
				output3.append("".join(map(str,output2[i])))

		return output3


test = CardCount()
print test.dealHands(6,"012345012345012345")