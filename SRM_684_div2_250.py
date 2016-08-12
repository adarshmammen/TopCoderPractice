class Istr:
	def count(self, s, k):
		li = list(s)
		d = {}
		samp_li = []
		for ele in li:
			if d.has_key(ele):
				d[ele]+=1
			else:
				d[ele]=1
		for vals in d.values():
			samp_li.append(vals)

		print samp_li

		for i in range(k):
			samp_li[samp_li.index(max(samp_li))]-=1

		ret = [ele*ele for ele in samp_li]

		return sum(ret)


test = Istr()
print test.count('abacaba',0)


