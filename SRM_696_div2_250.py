class Ropestring:
	def makerope(self, s):
		ropes = [ele for ele in s.split('.') if ele != ""]
		lengths = [len(ele) for ele in ropes]
		even_l = [ele for ele in lengths if ele%2==0]
		odd_l = [ele for ele in lengths if ele%2!=0]
		s_even = sorted(even_l,reverse = True)
		s_odd = sorted(odd_l,reverse = True)

		final = []
		final.extend(s_even)
		final.extend(s_odd)
		ret = []

		for i,ele in enumerate(final):
			if i!=0 and len(ret)<=len(list(s)):
				ret.append('.')
			for i in range(ele):
				ret.append('-')
			
		while len(ret) != len(list(s)):
			ret.append('.')

		return ''.join(ret)



test = Ropestring()
print test.makerope('--..-.---..--')
print test.makerope('--.---')
print test.makerope('-.-')