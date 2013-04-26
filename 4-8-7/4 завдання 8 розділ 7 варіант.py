import nltk
from nltk.corpus import treebank
parsed_sents = treebank.parsed_sents()
parsed_sents[4]
print parsed_sents[4]
type(parsed_sents[4])
from nltk import Tree
help(Tree)
 parsed_sents[4].draw()
parsed_sents[4][0][0]
parsed_sents[4][0][0]
parsed_sents[4].node
for i in parsed_sents[4]:i.node 
for i in parsed_sents[4]:i.leaves
print i.leaves
for i in parsed_sents[4].productions():
  print i# print rules for grammar
for i in parsed_sents[4].productions():
	print i.rhs(), i.lhs()
for i in parsed_sents[4].productions():
	print i.is_nonlexical
