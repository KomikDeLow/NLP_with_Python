# Halyna Khimka
# Chapter 9.4
# Modify the grammar illustrated in (30) to incorporate a BAR feature for dealing
# with phrasal projections.
"""
This module contains the modified grammar with BAR feature which deals with phrasal projections.
It means that this grammas covers subordinate clauses.

"""

import nltk
from nltk import tree
from nltk import load_parser

"""
    S-> NP[NUM=?n] VP[TENSE=?t, NUM=?n]
    
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
    
    NP[NUM=sg] -> 'Kim'| 'He' | 'She' | 'It' | 'she'
    NP[NUM=pl] -> 'They'|'children' | 'People' | 'Girls'
    
    SBar -> Comp S
    Comp -> 'that'
"""
tokens='She claims that she likes children'.split()
cp = load_parser('grammars/book_grammars/Gram_Phr_Projections.fcfg')
for tree in cp.nbest_parse(tokens):
     print tree

tree.draw()


