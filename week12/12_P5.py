class Card:
	def __init__(self, value, suit):
		self.value=value
		self.suit=suit
		self.Index=["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
		self.IndexSuit=["club","diamond","heart","spade"]
	def __str__(self):
		return "("+self.value+" "+self.suit+")"
	def next1(self):
		if self.IndexSuit.index(self.suit)==3:
			if self.Index.index(self.value)==12:
				return Card(self.Index[0],self.IndexSuit[0])
			else:
				return Card(self.Index[self.Index.index(self.value)+1],self.IndexSuit[0])
		else:
			return Card(self.value,self.IndexSuit[self.IndexSuit.index(self.suit)+1])
	def next2(self):
		if self.IndexSuit.index(self.suit)==3:
			if self.Index.index(self.value)==12:
				self.value=self.Index[0]
				self.suit=self.IndexSuit[0]
			else:
				self.value=self.Index[self.Index.index(self.value)+1]
				self.suit=self.IndexSuit[0]
		else:
			self.value=self.value
			self.suit=self.IndexSuit[self.IndexSuit.index(self.suit)+1]
n = int(input())
cards = []
for i in range(n):
	value, suit = input().split()
	cards.append(Card(value, suit))
for i in range(n):
	print(cards[i].next1())
print("----------")
for i in range(n):
	print(cards[i])
print("----------")
for i in range(n):
	cards[i].next2()
	cards[i].next2()
	print(cards[i])
