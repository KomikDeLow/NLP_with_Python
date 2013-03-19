# TODO
# It isn't Python modul
# I don't see words that "are more common in their plural form"
#
#

>>> import nltk
>>> from nltk.corpus import brown
>>> cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in brown.tagged_words(categories = 'news'))
>>> singular_nouns = cfd['NN'].keys()
>>> plural_nouns = cfd['NNS'].keys()
>>> s = brown.tagged_words(categories = 'news')
>>> for word in plural_nouns[:20]:
	print word, ':', s.count((word, 'NNS'))

	
years : 101
members : 69
people : 52
sales : 51
men : 46
children : 45
months : 42
days : 37
schools : 36
laws : 30
runs : 30
bonds : 28
countries : 28
funds : 27
minutes : 25
weeks : 25
persons : 24
police : 23
efforts : 22
games : 22
>>> for word in singular_nouns[:20]:
	print word, ':', s.count((word, 'NN'))

	
year : 137
time : 97
state : 88
week : 85
home : 72
man : 72
program : 65
school : 65
night : 64
day : 61
meeting : 58
president : 53
administration : 52
government : 52
cent : 51
game : 51
tax : 51
car : 49
city : 49
board : 47
>>> 
