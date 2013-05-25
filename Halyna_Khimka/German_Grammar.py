# Halyna Khimka
# Chapter 9.5
# Modify the German grammar in Example 9-4 to incorporate the treatment of
# subcategorization presented in Section 9.3.
"""
This module uses modified german grammar with the category of subcategorisation of transitive and intransitive verbs in German language.
Transitive verbs have an object in accusative or dative case.
Intransitive verbs don't require any object. 
"""
import nltk
from nltk import load_parser
from nltk import tree

tokens = 'ich folge den Katzen'.split()
cp = load_parser('grammars/book_grammars/german_grammar.fcfg')
for tree in cp.nbest_parse(tokens):
    print tree

tree.draw()

