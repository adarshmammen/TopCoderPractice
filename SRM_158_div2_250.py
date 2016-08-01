class TireRotation:
	def getCycle(self, initial, current):
		a = list(initial)
		count = 1

		if initial == current:
			return 1
		else:
			while "".join(a) != current:
				a = a[3]+a[2]+a[0]+a[1]
				print a
				count+=1
				if a == current:
					return count
				if a == initial:
					return -1






test = TireRotation()

print test.getCycle("ABCD","DCAB")






