#coloring and randomness
from colorama import Back

class wordle:	
	#formatting
	def correct(self, stri):
		return Back.GREEN + stri + Back.RESET
	
	def isthere(self, stri):
		return Back.YELLOW + stri + Back.RESET
	
	def incorrect(self, stri):
		return Back.RED + stri + Back.RESET

	#inits wordand custom formatting if formatting exists
	def __init__(self, word, corr=None, ist=None, inc=None):
		self.word = word
		if corr != None:
			self.correct = corr
		if ist != None:
			self.isthere = corr
		if inc != None:
			self.incorrect = corr
	
	def checker(self, iword):
		word = self.word
		h = [None] * len(word)
		user = [None] * len(word)
		corr = [None] * len(word)
		corrcp = [None] * len(word)
		for i, k in enumerate(iword):
			if k == word[i]:
				h[i] = self.correct(iword[i])
			else:
				user[i] = iword[i]
				corr[i] = word[i]
				corrcp[i] = word[i]
		for i, k in enumerate(user):
			if k in corr and k != None:
				h[i] = self.isthere(iword[i])
				corr.pop(corr.index(k))
			elif k != corrcp[i]:
				h[i] = self.incorrect(iword[i])
		return h