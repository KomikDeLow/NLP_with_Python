# Petrukha Tetiana Als-11
# Chapter_9, Ex_7

# Develop a wrapper for the earley_parser so that a trace is only printed
# if the input sequence fails to parse.

import nltk
from nltk import load_parser # import the load_parser function
tokens = 'Jody likes dogs'.split()
cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=1) # returns a chart parser cp
trees = cp.nbest_parse(tokens) # return a list trees of parse trees
