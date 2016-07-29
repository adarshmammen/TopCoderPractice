class DiskSpace:
	def minDrives(self, used, total):
		tot_used = sum(used)
		add_check =tot_used

		for i,ele in enumerate(sorted(total)[::-1]):
			add_check -= ele
			if add_check <=0:
				return i+1
		return -1



test = DiskSpace()

print test.minDrives([448, 499, 29, 477, 534, 548, 62, 326, 695, 460, 384, 706, 269, 216, 602, 822, 60, 321, 85, 369, 641, 934, 242],
					 [702, 911, 132, 673, 823, 550, 973, 893, 984, 517, 639, 810, 619, 536, 860, 849, 939, 479, 610, 962, 808, 939, 919])






