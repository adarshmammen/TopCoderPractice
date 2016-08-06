class Pool:
	def rackMoves(self, triangle):
		triangle_conv = self.convert(triangle)
		goodconfig1, goodconfig2 = list("XOOX8XOXOXXOXOO"), list("OXXO8OXOXOOXOXX")
		diff = [0,0]
		
		for i,ele in enumerate(triangle_conv):
			if ele != goodconfig1[i]:
				diff[0]+=1
			if ele != goodconfig2[i]:
				diff[1]+=1
		for i in range(2):
			if diff[i]%2!=0:
				diff[i]+=1	

		return min(diff)/2		

	def convert(self, str1):
		out = []
		for ele in list(str1):
			if ele<8:
				out.append('O')
			elif ele == 8:
				out.append('8')
			else:
				out.append('X')
		return out




test = Pool()
print test.rackMoves([2, 10, 7, 1, 8, 12, 6, 11, 4, 9, 13, 3, 14, 15, 5])
print test.rackMoves([8, 15, 9, 4, 10, 6, 11, 3, 14, 7, 2, 1, 13, 12, 5])
print test.rackMoves([15, 5, 8, 13, 2, 14, 10, 3, 4, 6, 7, 9, 1, 12, 11])