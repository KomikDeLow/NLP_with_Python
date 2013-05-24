#by Ivanna Kushniruk
#Develop a variant of grammar in Example 9-1 that uses a feature COUNT to make
#the distinctions shown here:
#(56) a. The boy sings.
#b. *Boy sings.
#(57) a. The boys sing.
#b. Boys sing.
#(58) a. The water is precious.
#b. Water is precious.


import nltk
token1 = 'The boy sings'.split() #define tokens
token2 = 'Boy sings'.split()
token3 = 'The water is precious'.split()
from nltk import load_parser #import load_parser
cp = load_parser('grammars/book_grammars/feat0_Ivanka.fcfg', trace=2) #define parser
print token1
trees = cp.nbest_parse(token1) #show tree for sentence in token1
print token2
trees = cp.nbest_parse(token2)
print token3
trees = cp.nbest_parse(token3)



