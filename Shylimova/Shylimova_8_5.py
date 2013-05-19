# Shylimova K. Al-13
# Chapter 8, task 5

import nltk 
groucho_grammar1 = nltk.parse_cfg(""" 
    S -> NP  
    NP -> Adj NP 
    NP -> N Cnj N  
    N -> 'men' | 'women' 
    Adj -> 'old' 
    Cnj -> 'and' 
    """) 
sent1 = ['old', 'men', 'and', 'women'] 
parser = nltk.ChartParser(groucho_grammar1) 
trees = parser.nbest_parse(sent1) 
for tree1 in trees: 
    print 'A'
    print tree1 # task A
import nltk 
groucho_grammar1 = nltk.parse_cfg(""" 
    S -> NP 
    NP -> AdjNP Conj N 
    AdjNP -> Adj N 
    N -> 'men' | 'women' 
    Adj -> 'old' 
    Conj -> 'and' 
    """) 
sent1 = ['old', 'men', 'and', 'women'] 
parser = nltk.ChartParser(groucho_grammar1) 
trees = parser.nbest_parse(sent1) 
for tree1 in trees: 
    print 'A'
    print tree1 # task A
import nltk
groucho_grammar2 = nltk.parse_cfg(""" 
    S -> NP VP 
    NP -> Det N 
    VP -> VP AdPr | V NP 
    AdPr -> Adj PropNoun 
    Det -> 'a' | 'The' 
    N -> 'woman' | 'man' 
    V -> 'saw' 
    Adj -> 'last' 
    PropNoun -> 'Thursday' 
    """) 
sent2=['The', 'woman', 'saw', 'a', 'man', 'last', 'Thursday'] 
parser = nltk.ChartParser(groucho_grammar2) 
trees = parser.nbest_parse(sent2) 
for tree2 in trees: 
    print 'C'
    print tree2 # task C

for tree1 in trees:
    tree1.draw() # task B


