class BearNSWE:
	def totalDistance(self, a, dir):
		import math as m
		dir_list = map(int, a)
		pos = [0,0]
		
		for i in range(0,len(dir_list)):

			if dir[i] == 'N':
				pos[0] += dir_list[i]
			if dir[i] == 'S':
				pos[0] -= dir_list[i]
			if dir[i] == 'E':
				pos[1] += dir_list[i]
			if dir[i] == 'W':
				pos[1] -= dir_list[i]
		print pos
				
		ret = m.sqrt(pos[0]*pos[0] + pos[1]*pos[1])
		ret += sum(dir_list)
		return ret


test = BearNSWE()

print test.totalDistance((1,3,3,), "NES")