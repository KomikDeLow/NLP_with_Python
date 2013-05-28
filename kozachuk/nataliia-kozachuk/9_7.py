##9_7
import nltk
from nltk import load_parser# import load parser
tokens = 'Kim likes cars'.split()
cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=1)#return parser
trees = cp.nbest_parse(tokens)#return a tree
