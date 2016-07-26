class MostProfitable:
	def bestItem(self, costs, prices, sales, items):
		best = 0
		stored_i =0
		flag = 0
		for i in range(len(items)):
			profit_or_loss = (prices[i] - costs[i]) *sales[i]
			if profit_or_loss > best:
				best = profit_or_loss
				flag = 1
				stored_i = i

		return items[stored_i] if flag !=0 and best>=0 else ""





test = MostProfitable()

print test.bestItem([38,24],[37,23],[1000,643],["Letter","Postcard"])
print test.bestItem([10,10],[11,12],[2,1],["A","B"])






