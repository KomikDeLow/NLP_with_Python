#Chapter_9_Ex_5_Mokhonova
import nltk
from nltk import load_parser
tokens = 'ich folge den Katzen'.split()# pryklad rechennya
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')#funciya parse.load_parser dozvolyaje chytaty gramatyku v NLTK,
for tree in cp.nbest_parse(tokens):
	print tree

tokens = 'du kommst '.split()# pryklad rechennya
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree

tokens = 'die Katze hilft dem Hund '.split()# pryklad rechennya
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree

