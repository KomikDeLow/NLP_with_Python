# Olesya Mykhaulyk ALs-12
#Chapter 8 Ex 4
import nltk
from nltk import Tree
help(Tree) # looking at Tree class documentation
grammar1=nltk.parse_cfg("""
S->VP CC VP
VP->VP CC VP|NV|NP V|V
V->"arrived"|"left"|"cheered"
NP->"Kim"|"Dana"
N->"everyone"
CC->"and"|"or"
""")
sent='Kim arrived or Dana left and everyone cheered'.split() # I test some methods from examples
cparser=nltk.ChartParser(grammar1)# I'm bringing the tree to the normal Chomsky's form
a=cparser.parse(sent)# using the grammar from the example presented in the chapter
a.chomsky_normal_form()
print a
