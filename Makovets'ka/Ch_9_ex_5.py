#Modify the German grammar in Example 9-4 to incorporate the treatment
#of subcategorization presented in Section 9.3.

import nltk
from nltk import load_parser
tokens = 'wir folgen den Katzen'.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
    print tree

tokens = 'wir kommen '.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
    print tree

tokens = 'wir helfen den Katzen '.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
    print tree
