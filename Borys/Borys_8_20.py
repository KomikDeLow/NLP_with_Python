import nltk
from nltk import tree
from nltk.draw.tree import draw_trees # first tree
groucho_grammar = nltk.parse_cfg("""
    S -> NP VP
    NP -> Det N
    VP -> VP AP | V NP
    AP -> Adj PropN
    Det -> 'a' | 'The'
    N -> 'woman' | 'man'
    V -> 'saw'
    Adj -> 'last'
    PropN -> 'Thursday'
    """)
sent=['The', 'woman', 'saw', 'a', 'man', 'last', 'Thursday']
parser = nltk.ChartParser(groucho_grammar)
tree1 = parser.nbest_parse(sent) # second tree
groucho_grammar2 = nltk.parse_cfg("""
    S -> NP
    NP -> Adj NP
    NP -> N Conj N
    Conj -> 'and'
    N -> 'woman' | 'man'
    Adj -> 'old'
    """)
parser2 = nltk.ChartParser(groucho_grammar2)
sent2=['old', 'man', 'and', 'woman']
tree2 = parser2.nbest_parse(sent2)
# using draw_trees()
draw_trees(tree1, tree2)
