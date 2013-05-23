#Bilous Volodymyr, Al-11,
#chapter 9, task 4
import nltk
from nltk import load_parser #import the load_parser function
parser = load_parser('grammars/book_grammars/feat0.fcfg')
tokens = 'girl walks'.split() 
parser = load_parser('grammars/book_grammars/feat0.fcfg')
for tree in parser.nbest_parse(tokens):    # data- tree output 
         print tree
#We modify the grammar Illustrated in (30) to incorporate a BAR feature for dealing with phrasal projections.
