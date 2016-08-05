class LCMRange:
	def lcm(self, first, last):
		rem = 0
		for i in range(first,last+1):
			if i == first:
				rem = self.lcm2(i,i)
			else:
				rem = self.lcm2(rem,i)
		return rem
	def lcm2(self,a,b):
		gcd, tmp = a,b
		while tmp != 0:
			gcd,tmp = tmp, gcd % tmp
		return a*b/gcd	

test = LCMRange()
print test.lcm(1,5)

