# Chubko Uliana AL-12
import nltk
from nltk import *
sent = [ 'She', 'kills','the','boy','in','her','story']
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
    # будуємо рекурсивну функцію для першого дерева
    t=nltk.Tree('(S(NP I)(VP(V shot)(NP (Det an) (N elephant) (PP (P in) (NP (Det my) (N pajamas))))))')
def traverse (t):
    # рекурсивна функція:
     try:                    
        t.node
    except  AttributeError :
        print t,
    else:
        print '(', t.node,
        for child in t:
        
             traverse(child)  
        print ')',
print t.height() 
nltk.Tree.draw (t)
    
         
