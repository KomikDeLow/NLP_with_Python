import nltk
# load our grammar
nltk.data.show_cfg('grammars/book_grammars/PM_german.fcfg')
# define the sentence with mistake and split it
tokens = 'Heute sieht der Hund der Katze'.split()
# set the trace parameter of the load_parser()
from nltk import load_parser
# get an idea where and why a sequence fails to parse and use trace parameter to controls the parser reports the steps that it takes as it parses a text
cp = load_parser('grammars/book_grammars/PM_german.fcfg', trace=2)
for tree in cp.nbest_parse(tokens):
	print tree
