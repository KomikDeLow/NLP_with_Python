##8_5a
import nltk#parsing with grammar
groucho_grammar = nltk.parse_cfg("""  
        S -> NP 
        NP -> Adj NP
        NP -> N Cnj N 
        N -> 'men' | 'women'
        Adj -> 'old'
        Cnj -> 'and'
        """)
sent = ['old', 'men', 'and', 'women']#our sentence
parser = nltk.ChartParser(groucho_grammar)
trees = parser.nbest_parse(sent)
for tree in trees:
	print tree#results

	    

import nltk
groucho_grammar = nltk.parse_cfg("""
        S -> NP
        NP -> AdjNP Conj N
        AdjNP -> Adj N
        N -> 'men' | 'women'
        Adj -> 'old'
        Conj -> 'and'
        """)
sent = ['old', 'men', 'and', 'women']
parser = nltk.ChartParser(groucho_grammar)
trees = parser.nbest_parse(sent)
for tree in trees:
	    print tree
