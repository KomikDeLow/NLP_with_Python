# TODO
# It isn't the Python modul
#
Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def persentage(text)
SyntaxError: invalid syntax
>>> import nltk
>>> from nltk.corpus import brown
>>> def persentage(text):
	data=nltk.ConditionalFreqDist((word.lower(),tag) for (word,tag)in text)
	t=0
	a=0
	for word in data.conditions():
		if len(data[word])==1:
			a+=1
		t+=1
	return a*100/t

>>> persentage(nltk.corpus.brown.tagged_words())
80
>>> persentage(nltk.corpus.treebank.tagged_words())
87
>>> 
