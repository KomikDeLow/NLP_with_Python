# Iuliia Tsymbalista
# chapter 9 ex.4
# corrected
# this is modified grammar from example 30, with a BAR feature.


import nltk
from nltk import *


"""
S -> NP[NUM=?n] VP[TENSE=?T, NUM=?n]

    NP[NUM=sg] -> 'she'
    NP[NUM=pl] -> 'They'|'candies' | 
	
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
    
	SBar -> BR NP S # this means that after BR component noun should be placed
	NP[NUM=sg] -> 'she' 
	BR -> 'that'
	
"""
tokens = 'They say that she likes candies'.split()
cp =load_parser('grammars/book_grammars/my_grammar_modified.fcfg')
for tree in cp.nbest_parse(tokens):
    print tree

tree.draw()
