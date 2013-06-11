# Chapter_9_Ex_5_Fursachyk
import nltk
from nltk import load_parser   # завантаження функції граматичного розбору
tokens = 'ich folge den Katzen'.split() # приклад речення
cp = load_parser('grammars/book_grammars/german.fcfg') # список дерев граматичного розбору
for tree in cp.nbest_parse(tokens):
	print tree                                  # виведення дерева


from nltk import load_parser
tokens = 'die Katze hilft dem Hund '.split()
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree

tokens = 'du kommst '.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree
