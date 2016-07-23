class BearCharges:
	def minTime(self, x, y):
		import math as m
		N = len(x)
		bases_left = range(N)
		dist_mat = []
		captured = [0]

		for i in range(N):
			temp = []
			for j in range(N):
				temp.append(m.sqrt(pow((x[i]-x[j]),2) + pow((y[i]-y[j]),2)))

			dist_mat.append(temp)

		time = 0
		splice = 1
		bases_left.remove(0)

		time += min(dist_mat[0][splice:])
		captured.append(dist_mat[0].index(min(dist_mat[0][splice:])))

		bases_left.remove(dist_mat[0].index(min(dist_mat[0][splice:])))

		base_min = 99999999999
		remember_i = []
		remember_j = []	
		prev_capture = []

		while bases_left != []:
			flag = 0

			for z in range(1,N):
				for i in captured:
					for j in bases_left:
						temp_min = dist_mat[i][j]
						if temp_min<=base_min and flag == 0:
							base_min = temp_min
							remember_j, remember_i = j, i 

						if temp_min == base_min and flag == 1:
							remember_i,remember_j =j,i

					
				flag = 1
				if prev_capture == captured:
					break		
			
				bases_left.remove(remember_j)
				captured.append(remember_j)

				prev_capture = captured

					

			for i in captured:
				for j in bases_left:
					dist_mat[i][j]-= base_min

			time+=base_min
			base_min = 99999999999
		return time

			



test = BearCharges()

print test.minTime([10, 11, 12],[0, 0, 1])
print test.minTime([0,0,0,-1,1],[1,0,-1,0,0])





