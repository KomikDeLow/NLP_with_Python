"""
The same as with "German_grammar.py"
"""

#Presented by Tetiana Kobryn

#Chapter 9, Ex.2
#Develop a variant of grammar in Example 9-1 that uses a feature COUNT to make
#the distinctions shown here:
#(56) a. The boy sings.
#b. *Boy sings.
#(57) a. The boys sing.
#b. Boys sing.
#(58) a. The water is precious.
#b. Water is precious.


import nltk

#renewed grammar:
"""
    S -> NP[NUM=?n] VP[NUM=?n]

    # NP expansion productions 
    NP[NUM=?n] -> PropN[NUM=?n] 
    NP[NUM=pl, COUNT=c] -> Det[NUM=pl] N[NUM=pl, COUNT=c]
    NP[COUNT=un] -> Det[NUM=sg] N[COUNT=un]
    NP[COUNT=un] -> N[COUNT=un]
    NP[NUM=pl, COUNT=c] -> N[NUM=pl, COUNT=c] 
    NP[NUM=sg, COUNT=c] -> Det[NUM=sg] N[NUM=sg, COUNT=c]

    # VP expansion productions
    VP[TENSE=?t, NUM=?n] -> Cop[TENSE=?t, NUM=?n] Adj
    VP[TENSE=?t, NUM=?n] -> IV[TENSE=?t, NUM=?n]
    VP[TENSE=?t, NUM=?n] -> TV[TENSE=?t, NUM=?n] NP

    # ###################
    # Lexical Productions
    # ###################

    Det[NUM=sg] -> 'this' | 'every'
    Det[NUM=pl] -> 'these' | 'all'
    Det -> 'the' | 'some' | 'several' | 'The'

    PropN[NUM=sg]-> 'Kim' | 'Jody'

    N[NUM=sg, COUNT=c] -> 'dog' | 'girl' | 'car' | 'child' | 'boy' | 'Boy'
    N[NUM=pl, COUNT=c] -> 'dogs' | 'girls' | 'cars' | 'children'| 'boys'| 'Boys'

    N[COUNT=un] -> 'water' | 'Water'

    IV[TENSE=pres,  NUM=sg] -> 'disappears' | 'walks' | 'sings'
    TV[TENSE=pres, NUM=sg] -> 'sees' | 'likes'

    IV[TENSE=pres,  NUM=pl] -> 'disappear' | 'walk'| 'sing'
    TV[TENSE=pres, NUM=pl] -> 'see' | 'like'

    IV[TENSE=past] -> 'disappeared' | 'walked'
    TV[TENSE=past] -> 'saw' | 'liked'

    Cop[TENSE=pres, NUM=sg] -> 'is'
    Adj -> 'precious'
"""
#define tokens
token1 = 'The boy sings'.split()
token2 = 'Boy sings'.split()
#import load_parser
from nltk import load_parser
#define chart parser
cp = load_parser('grammars/book_grammars/feat0_new2.fcfg', trace=2)
#presenting results
print "token1 = 'The boy sings'"
trees = cp.nbest_parse(token1)
print
print "token2 = 'Boy sings'"
trees = cp.nbest_parse(token2)



