class PaperFold:
	def numFolds(self, paper, box):
		count = 0
		if ((box[0] - paper[0]) > 0 and (box[1] - paper[1]) > 0) or ((box[0] - paper[1]) > 0 and (box[1] - paper[0]) > 0):

			return count 
		else:
			while paper and ((paper[paper.index(max(paper))] > box[box.index(max(box))]) or (paper[paper.index(min(paper))] > box[box.index(min(box))])):
				paper[paper.index(max(paper))] = float(paper[paper.index(max(paper))])/2
				count+=1
				if paper[paper.index(max(paper))] < box[box.index(max(box))]:
					del paper[paper.index(max(paper))], box[box.index(max(box))]

			return count if count<=8 else -1


		return paper,box



test = PaperFold()
print test.numFolds([7983, 4143], [9349, 1122])