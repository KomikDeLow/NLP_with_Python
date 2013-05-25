

import nltk
# define the grammar
groucho_grammar = nltk.parse_cfg("""
       S -> NP VP
       PP -> P NP
       NP -> Det N | Det N VP
       VP -> V PP | V
       Det -> 'The' | 'the'
       N -> 'horse' | 'barn'
       V -> 'raced' | 'fell'
       P -> 'past'
       """)
# define our sentence
sent = ['The', 'horse', 'raced', 'past', 'the', 'barn', 'fell']
# analyze our grammar using ChartParser
parser = nltk.ChartParser(groucho_grammar)
trees = parser.nbest_parse(sent)
# display results
for tree in trees:
    print tree
