class Time:
	def whatTime(self, seconds):
		h = int(seconds/3600)
		m = int(seconds/60)
		while m >=60:
			m = m -60
		s = seconds - (h*3600 + m*60)
		return ':'.join(map(str,[h,m,s]))


seconds = Time()
print seconds.whatTime(86399)
print seconds.whatTime(5436)
print seconds.whatTime(3661)