# Komar Mariia Als-11
# Chapter_9, Ex_2

# Develop a variant of grammar in Example 9-1 that uses a feature COUNT
# to make the distinctions shown here:
# (56) a. The boy sings.
# b. *Boy sings.
# (57) a. The boys sing.
# b. Boys sing.
# (58) a. The water is precious.
# b. Water is precious.



import nltk
nltk.data.show_cfg('grammars/book_grammars/komar_ex_2.fcfg') #виводимо на екран створену граматику
print '----------tree----------'
tokens = ' boy sings'.split()
from nltk import load_parser #import the load_parser function
cp = load_parser('grammars/book_grammars/komar_ex_2.fcfg', trace=2)
for tree in cp.nbest_parse(tokens):
	print tree
  
## Komar Mariia Als-11
## Chapter_9, ex_2
#% start S
# ###################
# Grammar Productions
# ###################
# S expansion productions
#S -> NP[NUM=?n] VP[NUM=?n]
# NP expansion productions
#NP[NUM=?n] -> N[NUM=?n, Count=Uncountable] 
#NP[NUM=?n] -> Det[NUM=?n, Count=Countable] N[NUM=?n] 
# VP expansion productions
#VP[TENSE=?t, NUM=?n] -> IV[TENSE=?t, NUM=?n]
#VP[TENSE=?t, NUM=?n] -> TV[TENSE=?t, NUM=?n] Adj
# ###################
# Lexical Productions
# ###################
#Det -> 'the' 
#N[NUM=sg] -> 'boy' | 'water' 
#N[NUM=pl] -> 'boys'  
#IV[TENSE=pres,  NUM=sg] -> 'sings'
#TV[TENSE=pres, NUM=sg] -> 'is' 
#IV[TENSE=pres,  NUM=pl] -> 'sing'
#Adj -> 'precious'
