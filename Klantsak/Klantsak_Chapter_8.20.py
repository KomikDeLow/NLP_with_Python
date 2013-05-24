# Veronika KLantsak ALs-11
# compare multiple trees in a single window...

import nltk
from nltk import tree
from nltk.draw.tree import draw_trees # 1 tree
groucho_grammar = nltk.parse_cfg("""
    S -> NP VP
    NP -> Det N
    VP -> VP AP | V NP
    AP -> Adj PropN
    Det -> 'a' | 'The'
    N -> 'woman' | 'daughter'
    V -> 'waited'
    Adj -> 'hole'
    PropN -> 'Monday'
    """)
sent=['The', 'woman', 'waited', 'a', 'daugther', 'hole', 'Monday']
parser = nltk.ChartParser(groucho_grammar)
tree1 = parser.nbest_parse(sent) # 2 tree
groucho_grammar2 = nltk.parse_cfg("""
    S -> NP
    NP -> Adj NP
    NP -> N Conj N
    Conj -> 'and'
    N -> 'woman' | 'daughter'
    Adj -> 'young'
    """)
parser2 = nltk.ChartParser(groucho_grammar2)
sent2=['young', 'daughter', 'and', 'woman']
tree2 = parser2.nbest_parse(sent2) # using function draw_trees()
draw_trees(tree1, tree2)
