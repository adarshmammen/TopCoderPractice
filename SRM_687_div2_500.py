class Quacking:
	def quack(self, s):
		isValid =  self.valid(list(s))
		if not isValid:
			return -1
		else:
			testli = list(s)
			while 'k' in testli:
				ind = testli.index('k')
				for i in range(ind,len(testli)):
					if testli[i]=='q':
						isValid[1]-=1
						del testli[i]
						break
				del testli[ind]
			return isValid[1]


	def valid(self, s1):
		count1 = 0
		q_c = s1.count("q")
		u_c = s1.count("u")
		a_c = s1.count("a")
		c_c = s1.count("c")
		k_c = s1.count("k")
		if not q_c == u_c == a_c == c_c == k_c:
			return False
		li = list(s1)
		while li:
			q_ind = li.index('q')
			li.pop(q_ind) 
			if 'u' in li and li.index('u')>=q_ind:
				u_ind = li.index('u')
				li.pop(li.index('u'))

			else:
				return False
			if 'a' in li and li.index('a')>=u_ind:
				a_ind = li.index('a')
				li.pop(li.index('a'))
			else:
				return False
			if 'c' in li and li.index('c')>=a_ind:
				c_ind = li.index('c')
				li.pop(li.index('c'))
			else:
				return False
			if 'k' in li and li.index('k')>=c_ind:
				k_ind = li.index('k')
				li.pop(li.index('k'))
				count1+=1
			else:
				return False
		return [True, count1]



test = Quacking()
print test.quack("quqaquuacakcqckkuaquckqauckack")
print test.quack("quackqauckquack")
print test.quack("qqqqqqqqqquuuuuuuuuuaaaaaaaaaacccccccccckkkkkkkkkk")

