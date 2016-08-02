class StreetParking:
	def freeParks(self, street):
		street_list = list(street)
		b_flag, s_flag = 0,0
		count = 0
		prev_ele = ''
		prepre_ele = ''
		i = 0

		for ele in street_list[::-1]:
			
			if ele == '-' and not b_flag and not s_flag:
				count+=1
				count_flag = 1
				prev_ele = ele
			elif ele == 'B':
				b_flag=2
				prev_ele = ele
				if s_flag:
					s_flag-=1
			elif ele == 'S':
				if prev_ele == '-' and (not b_flag) and not(prepre_ele=='-'):
					count-=1
				s_flag =1
				prev_ele = ele
				if b_flag:
					b_flag-=1
			elif b_flag and s_flag:
				b_flag-=1
				s_flag-=1
				prev_ele = ele
			elif b_flag and not s_flag:
				b_flag-=1
				prev_ele = ele
			elif not b_flag and s_flag:
				s_flag-=1
				prev_ele = ele
			else:
				prev_ele = ele
				prepre_ele = prev_ele
				#continue
			if count < 0:
				count = 0
			if ele != '-':
				count_flag = 0
			print ele,count, b_flag,s_flag
			i+=1


			

		return count







test = StreetParking()

print test.freeParks("SSD-B---BD-DDSB-----S-S--------S-B----BSB-S--B-S-D")






