class WidgetRepairs:
	def days(self, arrivals, numPerDay):
		days = 0
		i = 0
		widgets_left = 0
		real_day = 0

		while i < len(arrivals) or widgets_left != 0:

			prev_wid = widgets_left
			#print widgets_left, days
			
			if i < len(arrivals):
				widgets_left += arrivals[i]


			if not (widgets_left== 0 and prev_wid == 0):

					days+=1

			i+=1
			widgets_left -=numPerDay

			if widgets_left < 0:
				widgets_left = 0			

		return days


test = WidgetRepairs()

print test.days([10,0,0,4,20],8)
print test.days([0,0,0],8)
print test.days([100,100],10)
print test.days([27,0,0,0,0,9],9)