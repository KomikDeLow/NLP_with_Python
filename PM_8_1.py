import nltk
# define a simple grammar
groucho_grammar = nltk.parse_cfg("""
    S -> NP VP
    PP -> P NP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    Det -> 'a' | 'my'
    N -> 'superstar' | 'house'
    V -> 'found'
    P -> 'in'
    """)
# define a sentence of my own
sent = ['I', 'found', 'a', 'superstar', 'in', 'my', 'house']
# analyze the sentence
parser = nltk.ChartParser(groucho_grammar)
trees = parser.nbest_parse(sent)
for tree in trees:
	print tree
