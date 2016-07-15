class CCipher:
	def decode(self, cipherText, shift):
		alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
		mainlist = []
		li1 = list(cipherText)
		
		for ele in li1:
			ind= alph.index(ele)+26 - shift
			mainlist.append(alph[ind])
		return ''.join(mainlist)

test = CCipher()
print test.decode("VQREQFGT", 2)