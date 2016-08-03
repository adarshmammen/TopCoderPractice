class Substitute:
	def getValue(self, key, code):
		key_list = list(key)
		code_list = list(code)
		output = []
		if code_list == []:
			return None
		
		for ele in code_list:
			if ele in key_list:
				output.append((key_list.index(ele)+1)%10)
		return int(''.join(map(str,output)))

test = Substitute()
print test.getValue('TRADINGFEW','LGXWEV')