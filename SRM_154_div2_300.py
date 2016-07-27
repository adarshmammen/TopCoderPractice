class ProfitCalculator:
	def percent(self, items):
		sold_tot, made_tot = [],[]
		for ele in items:
			sold, made = map(float,ele.split(" "))
			sold_tot.append(sold)
			made_tot.append(made)

		sum_sold, sum_made = sum(sold_tot), sum(made_tot)

		return int(((sum_sold - sum_made)/sum_sold)*100)

test = ProfitCalculator()

print test.percent([ "012.99 008.73","099.99 050.00","123.45 101.07" ])