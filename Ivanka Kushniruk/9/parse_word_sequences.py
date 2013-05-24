#by Ivanna Kushniruk
#my grammar 
"""S -> NP[AGR=?n] VP[TENSE=?t, AGR=?n]
NP[AGR=?n] -> PRP[AGR=?n]
VP[TENSE=?t, AGR=?n] -> Cop[TENSE=?t, AGR=?n] Adj
Cop[TENSE=pres, AGR=[NUM=sg, PER=3]] -> 'is'
Cop[TENSE=pres, AGR=[NUM=sg, PER=1]] -> 'am'
Cop[TENSE=pres, AGR=[NUM=pl, PER=2]] -> 'are'
Cop[TENSE=pres, AGR=[NUM=pl, PER=3]] -> 'are'
PRP[AGR=[NUM=sg, PER=1]] -> 'I'
PRP[AGR=[NUM=pl, PER=3]] -> 'they'
PRP[AGR=[NUM=pl, PER=2]] -> 'you'
PRP[AGR=[NUM=sg, PER=3]] -> 'she'
Adj -> 'happy'
"""

import nltk
token1 = 'I am happy'.split() #define tokens
token2 = 'you is happy'.split()
token3 = 'they am happy'.split()
from nltk import load_parser #import load_parser
cp = load_parser('grammars/book_grammars/Mine.fcfg', trace=2) #define parser
print token1
trees = cp.nbest_parse(token1) #show tree for sentence in token1
print token2
trees = cp.nbest_parse(token2)#show tree for sentence in token2
print token3
trees = cp.nbest_parse(token3) #show tree for sentence in token3

print """in token2 adj 'happy' exists, but not 'you is'. there is no "they am
happy" but 'am happy' exists"""
