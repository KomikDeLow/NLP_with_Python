#Прокулевич К. ПРЛс-11, Розділ 8, Задача 11
#With pen and paper, manually trace the execution of a recursive descent parser
#and a shift-reduce parser, for a CFG you have already seen, or one of your own
#devising.
import nltk
#simple context-free grammar:
grammar1 = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park"
P -> "in" | "on" | "by" | "with"
""")
#parsing a simple sentence admitted by the grammar:
sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.nbest_parse(sent):
    print tree
#graphical demonstration:
nltk.app.rdparser()
#parsing sentence with ShiftReduceParser:
sr_parse = nltk.ShiftReduceParser(grammar1)
sent = 'Mary saw a dog'.split()
print sr_parse.parse(sent)
#graphical demonstration:
nltk.app.srparser()
