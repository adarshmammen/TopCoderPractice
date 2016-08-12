class DivFreed2:
	def count(self, n, k):
		import itertools as it
		count = 0

		li = list(it.product(range(k+1),repeat=n))
		li = [ele for ele in li if ele[0]!=0]
		print li


		for nums in li:
			s = int("".join(map(str,nums)))
			print s
			
			tt = list(map(int,str(s)))
			print tt
			for i in range(len(tt)):
				if i == len(tt)-1:
					count+=1
					print "OK"
					break

				if tt[i+1]>=tt[i]:						
					#print "yes1"
					continue
				elif tt[i+1]!=0 and tt[i]%tt[i+1]!=0:						
					#print "yes2"
					continue
				else:
					break

		return count

		


test = DivFreed2()
print test.count(3,3)


