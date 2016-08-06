class CalendarRecycle:
	def useAgain(self, year):
		leap_orig =  self.leapcheck(year)
		count_wrap = 0
		for i in range(year+1,20000):
			if self.leapcheck(i):
				count_wrap+=2
			elif not self.leapcheck(i):
				count_wrap+=1
			if count_wrap%7==0 and self.leapcheck(i) == leap_orig:
				return i
		return -1

	def leapcheck(self,y):
		if y % 4 == 0:
			if y % 400 == 0:
				return True
			elif y % 100 == 0:
				return False
			else:
				return True
		else:
			return False

new = CalendarRecycle()
print new.useAgain(2002)