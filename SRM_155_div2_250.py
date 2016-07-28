class Quipu:
	def readKnots(self, knots):
		li = list(knots)
		li.pop(0)

		xflag = 1
		dashflag =0
		xcount =0
		dashcount =0
		final = []
		i = 0
		lenstore = len(li)

		for ele in li:
			i+=1
			print dashflag
			if i == lenstore and xflag == 0:
				final.extend([0]*(dashcount+1))
			if ele == 'X' and dashflag ==0:
				xcount+=1
				xflag = 1
			elif ele == '-' and xflag == 1:
				final.append(xcount)
				xcount =0
				xflag = 0
			elif ele == '-' and xflag == 0:
				dashcount+=1
				dashflag = 1
			elif ele == 'X' and dashflag ==1:
				final.extend([0]*dashcount)
				dashcount = 0
				dashflag = 0
				xflag = 1
				xcount+=1
			

		return int(''.join(map(str,final)))


test = Quipu()

print test.readKnots("-XXXX-XXXXX-XX-X-XXXX--")






