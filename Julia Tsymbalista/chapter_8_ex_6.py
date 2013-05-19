#Presented by Iuliia Tsymbalista
#chapter 8, ex. 6;


import nltk
from nltk import *
sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
groucho_grammar = nltk.parse_cfg("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")
parser = nltk.ChartParser(groucho_grammar)
trees = parser.nbest_parse(sent)
for tree in trees:
    print tree

#for the first tree, i'm building a recursive function
t=nltk.Tree('(S(NP I)(VP(V shot)(NP (Det an) (N elephant) (PP (P in) (NP (Det my) (N pajamas))))))')
def traverse (t):
    
#building a recursive funtion
    try:                    
        t.node
    except  AttributeError :
        print t,
    else:
        print '(', t.node,
        for child in t:
            
# traversing a treebank            
               traverse(child)  
        print ')',
print t.height() 
nltk.Tree.draw (t)
