# Yakymchuk / AL-12

import nltk
from nltk import tree
groucho_grammar = nltk.parse_cfg("""
    S -> NP
    NP -> Adj NP
    NP -> N Conj N
    Conj -> 'and'
    N -> 'woman' | 'man'
    Adj -> 'old'
    """)
parser = nltk.ChartParser(groucho_grammar)
sent=['old', 'man', 'and', 'woman']
trees = parser.nbest_parse(sent)
for tree in trees:
	print tree

#(S (NP (Adj old) (NP (N man) (Conj and) (N woman))))