# Shylimova K. Al-13
# Chapter 8, task 8

import nltk
grammar = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "call"
NP -> "Sue" | "Ann" | "Sam" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "book" | "table" | "cafe"
P -> "in" | "on" | "by" | "with"
""")
rd_parser = nltk.RecursiveDescentParser(grammar)
sent = 'Sue saw a dog'.split()
for t in rd_parser.nbest_parse(sent):
    print t 
sent = 'Ann call Sam'.split() 
for t in rd_parser.nbest_parse(sent):
    print t 
sent = 'Sam saw a book on the table'.split() 
for t in rd_parser.nbest_parse(sent):
    print t
sent = 'Sue saw Sam with a book'.split() 
for t in rd_parser.nbest_parse(sent):
    print t
sent = 'Sue saw Sam with a book in the cafe'.split()
for t in rd_parser.nbest_parse(sent):
    print t
