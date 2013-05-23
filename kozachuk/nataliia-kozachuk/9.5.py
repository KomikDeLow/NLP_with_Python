#nataliia kozachuk 9_5
import nltk
from nltk import load_parser
tokens = 'wir folgen den Katzen'.split()# pruklad rechennja
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree


tokens = 'wir kommen '.split()# pruklad
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree

tokens = 'wir helfen den Katzen '.split()#pruklad
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree
#The grammar  illustrates the
#comprising person, number and gender) with case.
