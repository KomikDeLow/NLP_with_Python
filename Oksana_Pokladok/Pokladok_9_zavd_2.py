#Pokladok Oksana
import nltk
nltk.data.show_cfg('grammars/book_grammars/komar_ex_2.fcfg') 
print '----------tree----------'
tokens = ' boy sings'.split()
from nltk import load_parser #import the load_parser function
cp = load_parser('grammars/book_grammars/komar_ex_2.fcfg', trace=2)
for tree in cp.nbest_parse(tokens):
	print tree