class DivisorDigits:
	def howMany(self, number):
		num_list1 = map(int, str(number))
		#num_list2 = [ele for ele in numlist1 if ele !=0]
		count = 0
		
		for ele in num_list1:
			if ele != 0 and number%ele == 0:
				count+=1
				
		return count

test = DivisorDigits()
print test.howMany(12345)