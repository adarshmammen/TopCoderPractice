class TriangleEasy:
	def find(self, n, x, y):
		d={}
		if not x:
			return 3

		n_ind = len(x)
		for i in range(n_ind):
			#if not x[i]:
				#break
			val = min(x[i],y[i])
			if not d.has_key(val):
				d[val] = []
				d[val].append(max(x[i],y[i]))
			else:
				d[val].append(max(x[i],y[i]))

		print d.items()
		for keys in d.keys():
			if len(d[keys])>1:
				for ele in d[keys]:
					if d.has_key(ele):
						temp_li = [e for e in d[keys] if e != ele]
						for z in d[ele]:
							if z in temp_li:
								return 0
			


				return 1

		return 2





test = TriangleEasy()
print test.find(4,[0,2,1,2],[3,0,2,3])
print test.find(3,[0,1],[1,2])


