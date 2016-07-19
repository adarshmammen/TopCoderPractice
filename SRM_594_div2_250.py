class FoxAndClassroom:
	def ableTo(self, n, m):
	
		combos = []
		
		for i in range(0,n*m):
			j = range(n*m,-1,-1)
			i_app = i%n
			j_app = abs(j[i])%m
			#print i_app, j_app
			if (i_app, j_app) not in combos:
				combos.append((i_app,j_app))
		print combos
					
		return "Possible" if len(combos)== n*m else "Impossible"
		

test = FoxAndClassroom()

print test.ableTo(2,3)
print test.ableTo(2,2)
print test.ableTo(5,7)