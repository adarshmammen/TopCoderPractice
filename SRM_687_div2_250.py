class Quorum:
	def count(self, arr, k):
		li = sorted(arr)
		return sum(li[:k])


test = Quorum()
print test.count([5,2,3],1)
