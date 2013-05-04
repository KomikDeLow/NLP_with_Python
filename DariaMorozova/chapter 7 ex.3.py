# Daria Morozova
# AL-12
# variant 11
# Chapter 7 Exercise 3






import nltk
from nltk.corpus import conll2000  # importing CoNLL-2000 Chunking corpus
sentence=[('Robert','NNP'),('Delanely','NNP'),('a','DT'),('consultant','NN'),('at','IN'),('Arthur','NNP'),('Inc.','NNP'),('said','VBD'),('We','PRP'),
	  ('have','VBP'),('gotten','VBN'),('all','PDT'),('the','DT'),('benefits','NNS'),('of','IN'),('deregulation','NN'),('in','IN'),('freight-cost','JJ'),
	  ('reductions','NNS'),(".",".")]
grammar = "NP: {<DT>?<JJ>*<NN>}" #creating a rule for the grammar
cp = nltk.RegexpParser(grammar) #using a grammar I create a chunk parser
result = cp.parse(sentence) #test it on my sentence
print result #print our results as a tree

