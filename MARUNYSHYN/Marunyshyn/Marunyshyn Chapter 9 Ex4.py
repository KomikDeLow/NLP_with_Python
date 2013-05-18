# Irena Marunyshyn PRLs-12
#Modify the grammar illustrated in (30) to incorporate a BAR feature for dealing
#with phrasal projections
import nltk
from nltk import load_parser
tokens = 'Kim likes children'.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat0.fcfg')# the function parse.load_parser allows us to read the grammar into NLTK, ready for use in parsing.
for tree in cp.nbest_parse(tokens):
	print tree
tokens = 'Kim likes child'.split()
from nltk import load_parser
p = load_parser('grammars/book_grammars/feat0.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree	
tokens = 'girl walked'.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat0.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree

# with the help of this program we can work with grammar. we can see the tense
# of the word, plural or singural, or this word transitive or intransitive
# if we use the word (walked) in past tense, the program will show us that there is
# no numeral. for example, we can see the word children = pl, and the child = sg.
