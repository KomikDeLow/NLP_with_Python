#Fuyarchuk O. Chapter 8 Task 5c
import nltk
groucho_grammar = nltk.parse_cfg("""
    S -> NP VP
    NP -> Det N
    VP -> VP AdP | V NP
    AdP -> Adj PropN
    Det -> 'a' | 'The'
    N -> 'woman' | 'man'
    V -> 'saw'
    Adj -> 'last'
    PrN -> 'Thursday'
    """)
sent=['The', 'woman', 'saw', 'a', 'man', 'last', 'Thursday']
parser = nltk.ChartParser(groucho_grammar)
trees = parser.nbest_parse(sent)
for tree in trees:
        print tree
