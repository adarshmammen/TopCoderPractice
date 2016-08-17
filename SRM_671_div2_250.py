class BearPaints:
	def maxArea(self, W, H, M):
		d1 = {}
		d2 = {}
		w,h = W,H
		prod = W*H
		if prod<=M:
			return prod	
		else:
			prod_check = 1
			for i in range(w,0,-1):
				for j in range(h,0,-1):
					if d1.has_key(i)
					prod = i*j
					#print i,j,prod
					if prod>M:
						continue

					if prod>prod_check:
						prod_check = prod


			return prod_check



test = BearPaints()
#print test.maxArea(1000000,1000000,720000000007)
print test.maxArea(4,4,10)
print test.maxArea(1000000,12345,1000000000000)


