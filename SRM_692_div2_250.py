class PriorityQueue:
	def findAnnoyance(self, S, a):
		length = len(S)
		String = list(S)
		annoyance = 0

		for i in range(length):
			if String[i] == 'e':
				continue
			else:
				annoyance+=sum(a[:i])
		return annoyance





test = PriorityQueue()
print test.findAnnoyance("bbbbb",[1,1,1,1,1])
