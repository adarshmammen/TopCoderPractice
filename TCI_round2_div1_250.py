class Bullets:
    def match(self, guns, bullet):
    	from collections import deque as d 
    	q = d(bullet)
    	for i in range(0,len(q)):
    		test = self.check(list(q),list(guns))
    		if test != -1:
    			return test
    		else:
    			ele = q.popleft()
    			q.append(ele)
    	return -1


    def check(self, q, guns):
    	for i in range(0,len(guns)):
    		if q == list(guns[i]):
    			return i
    		else:
    			continue
    	return -1


a = Bullets()

print a.match(("| | | |","|| || |"," |||| "), "|| || |")