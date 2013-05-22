#Olesya Mykhaulyk
#ALs-12
#Chapter 9 ex7 
import nltk 
from nltk import load_parser 
tokens = 'ich folge den Katze'.split()
cp = load_parser('grammars/book_grammars/german.fcfg', trace=2) #returns a chart parser 
trees = cp.nbest_parse(tokens) #Calling the parser�s nbest_parse() method 
#will return a list trees of parse trees
