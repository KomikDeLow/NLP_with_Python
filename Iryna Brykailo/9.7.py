# Iryna Brykailo, ALs-13

import nltk
from nltk import load_parser
tokens = 'Jody likes dogs'.split()
cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=1) # returns a chart purser
trees = cp.nbest_parse(tokens)# returns a list of parsed trees
