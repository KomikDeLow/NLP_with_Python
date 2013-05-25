# Fuyarchuk O. Chapter 9 Task 4
#In the example of subcategorisation: by factoring subcategorization information
#out of the main category label, we could express more generalizations about
# properties of verbs.Not all phrases have heads.We also would like our grammar
#formalism to express the parent/head-child relation where it holds.
#X-bar syntax addresses this issue by abstracting out the notion of phrasal level.
import nltk
from nltk import tree
grammar=("""
S-> NP[NUM=?n, Prsn=?n] VP[TENSE=?t, NUM=?n, Prsn=?n]

VP[TENSE=?t, NUM=?n] -> V[SUBCAT=intrans, TENSE=?t, NUM=?n]
VP[TENSE=?t, NUM=?n] -> V[SUBCAT=trans, TENSE=?t, NUM=?n] NP
VP[TENSE=?t, NUM=?n] -> V[SUBCAT=clause, TENSE=?t, NUM=?n] SBar

V[SUBCAT=intrans, TENSE=pres, NUM=sg] -> 'disappears' | 'walks'
V[SUBCAT=trans, TENSE=pres, NUM=sg] -> 'sees' | 'likes'
V[SUBCAT=clause, TENSE=pres, NUM=sg] -> 'says' | 'claims'

V[SUBCAT=intrans, TENSE=pres, NUM=pl] -> 'disappear' | 'walk'
V[SUBCAT=trans, TENSE=pres, NUM=pl] -> 'see' | 'like'
V[SUBCAT=clause, TENSE=pres, NUM=pl] -> 'say' | 'claim'

V[SUBCAT=intrans, TENSE=past] -> 'disappeared' | 'walked'
V[SUBCAT=trans, TENSE=past] -> 'saw' | 'liked'
V[SUBCAT=clause, TENSE=past] -> 'said' | 'claimed'

NP[NUM=sg, Prsn=1] -> 'I' 
NP[NUM=pl, Prsn=1] -> 'We' 
NP[NUM=pl, Prsn=2] -> 'You'
NP[NUM=sg, Prsn=3] -> 'Jack'| 'She' | 'He' | 'It' 
NP[NUM=pl, Prsn=3] -> 'They'|'Kids' | 'Men' | 'Boys'  
SBar -> Comp S 
Comp -> 'which' 
""")
from nltk import load_parser
tokens = 'who like'.split()
cp = load_parser('grammars/book_grammars/feat1.fcfg')
parser = load_parser('grammars/book_grammars/feat1.fcfg')
for tree in parser.nbest_parse(tokens):
	print tree


print tree
