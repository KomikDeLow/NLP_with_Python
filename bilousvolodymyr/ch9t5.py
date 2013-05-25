#Bilous Volodymyr, AL-11
#Chapter 9, Task 5
import nltk
from nltk import load_parser
tokens = 'wir folgen den Hund'.split()#example sentence
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree


tokens = 'wir kommen '.split()#example
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree

tokens = 'wir helfen den Hund '.split()#example
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree

