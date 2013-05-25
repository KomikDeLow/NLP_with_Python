import nltk
from nltk import tree
grammar=("""
S-> NP[NUM=?n, Prsn=?n] VP[TENSE=?t, NUM=?n, Prsn=?n] 
VP[TENSE=?t, NUM=?n, Prsn=?n] -> V[SUBCAT=intrans, TENSE=?t, NUM=?n, Prsn=?n] 
VP[TENSE=?t, NUM=?n] -> V[SUBCAT=trans, TENSE=?t, NUM=?n] NP 
VP[TENSE=?t, NUM=?n, Prsn=?n] -> V[SUBCAT=clause, TENSE=?t, NUM=?n, Prsn=?n] SBar 
V[SUBCAT=intrans, TENSE=pres, NUM=sg, Prsn=3] -> 'disappears' | 'walks' 
V[SUBCAT=trans, TENSE=pres, NUM=sg, Prsn=3] -> 'sees' | 'likes' 
V[SUBCAT=clause, TENSE=pres, NUM=sg, Prsn=3] -> 'says' | 'claims' 
V[SUBCAT=trans, TENSE=pres, NUM=sg, Prsn=1] -> 'see' | 'like' 
V[SUBCAT=clause, TENSE=pres, NUM=sg, Prsn=1] -> 'say' | 'claim' 
V[SUBCAT=intrans, TENSE=pres, NUM=pl, Prsn=?n] -> 'disappear' | 'walk' 
V[SUBCAT=trans, TENSE=pres, NUM=pl, Prsn=?n] -> 'see' | 'like' 
V[SUBCAT=clause, TENSE=pres, NUM=pl, Prsn=?n] -> 'say' | 'claim' 
V[SUBCAT=intrans, TENSE=past] -> 'disappeared' | 'walked' 
V[SUBCAT=trans, TENSE=past] -> 'saw' | 'liked' 
V[SUBCAT=clause, TENSE=past] -> 'said' | 'claimed' 
NP[NUM=sg, Prsn=3] -> 'Kim'| 'He' | 'She' | 'It' 
NP[NUM=sg, Prsn=1] -> 'I' 
NP[NUM=pl, Prsn=1] -> 'We' 
NP[NUM=pl, Prsn=2] -> 'You' 
NP[NUM=pl, Prsn=3] -> 'They'|'Children' | 'People' | 'Girls'  
SBar -> Comp S 
Comp -> 'that' 
""")
from nltk import load_parser
tokens = 'who do you claim is that you like'.split()
cp = load_parser('grammars/book_grammars/feat1.fcfg')
parser = load_parser('grammars/book_grammars/feat1.fcfg')
for tree in parser.nbest_parse(tokens):
	print tree

