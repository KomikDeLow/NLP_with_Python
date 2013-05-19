#Presented by Iuliia Tsymbalista ALs-13
#Chapter 8, ex. 9
#Can the grammar in grammar1 (Example 8-1) be used to describe sentences that
#are more than 20 words in length?



import nltk
from nltk import *
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
sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.nbest_parse(sent):
    print tree

# for example:
#using grammar1 for the sentence that is 7 words in length
sent_1 = "John saw the cat in the park".split()
rd_parser_1 = nltk.RecursiveDescentParser(grammar1)
for tree_1 in rd_parser_1.nbest_parse(sent_1):
    print tree_1

#as the result we can see two trees,
#so this sentence is said to be structurally ambiguous.
