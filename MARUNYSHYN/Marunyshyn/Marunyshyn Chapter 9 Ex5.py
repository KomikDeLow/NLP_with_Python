#Irena Marunyshyn PRLs-12 Chapter 9 Ex5
# Modify the German grammar in Example 9-4 to incorporate the treatment of
# subcategorization presented in Section 9.3.
import nltk
from nltk import load_parser
tokens = 'ich folge den Katzen'.split()# example sentence
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')# the function parse.load_parser allows us to read the grammar into NLTK,
for tree in cp.nbest_parse(tokens):
	print tree

tokens = 'du kommst '.split()# example sentence
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree

tokens = 'die Katze hilft dem Hund '.split()# example sentence
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree
# So with the help of this program we can also work with different words in German.
# we can check parson, number and gender, which are difficult in this language.
# we can put the rules in a file where they can be edited, tested and revised.
