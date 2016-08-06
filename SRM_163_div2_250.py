class Inchworm:
	def lunchtime(self, branch, rest, leaf):
		eats = 0
		for i in range(branch+1):
			if i == 0:
				eats+=1
			elif i %rest ==0 and i % leaf ==0:
				eats+=1
		return eats



test = Inchworm()
print test.lunchtime(11,2,4)