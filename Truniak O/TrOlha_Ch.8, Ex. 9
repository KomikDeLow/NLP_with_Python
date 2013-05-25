# Presented by Olha Truniak, ALs-13
# Chapter 8, Ex.9

# Can the grammar in grammar1 (Example 8-1) be used to describe sentences that
# are more than 20 words in length?

import nltk
# A recursive context-free grammar:
trgrammar1 = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park"
P -> "in" | "on" | "by" | "with"
""")
sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(trgrammar1)
for tree1 in rd_parser.nbest_parse(sent):
    print tree1

"""But we can make one more sentence with every words
in this trgrammar1, but it can't describe sentences more than 20 words in length"""

# Ex.2 (one more sentence):

import nltk
# A recursive context-free grammar:
trgrammar1 = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park"
P -> "in" | "on" | "by" | "with"
""")
sent = "Mary walked in the park with a dog and saw Bob with a cat".split()
rd_parser = nltk.RecursiveDescentParser(trgrammar1)
for tree2 in rd_parser.nbest_parse(sent):
    print tree2

""" ValueError: Grammar does not cover some of the input words:'and'. """

    
