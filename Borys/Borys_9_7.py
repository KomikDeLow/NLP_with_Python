# Roman Borys PRLs-11
import nltk
from nltk import load_parser #importing load_parser function 
tokens = 'ich folge den Katze'.split() # tokenizing sentence
cp = load_parser('grammars/book_grammars/german.fcfg', trace=2) #returns a chart parser
#cp
trees = cp.nbest_parse(tokens) #Calling the parser’s nbest_parse() method
#will return a list trees of parse trees
