# Valerii Androshchuk APL(s)-13.
# Chapter 9, Task 4.
# Modify the grammar to incorporate a BAR feature for dealing with
# phrasal projections.

import nltk
tokens = 'you claim that you like cats'.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat1.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree
