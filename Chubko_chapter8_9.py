# Chubko Uliana AL-12
import nltk
from nltk import *
grammar1 = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "visited" | "slept" | "looked"
NP -> "Andrew" | "Ann" | "Peter" | Det N | Det N PP
Det -> "a" | "an" | "the" | "her"
N -> "boy" | "bull" | "cat" | "table" | "garden"
P -> "in" | "on" | "at" | "the"
""")
sent = "Andrew visited Ann".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.nbest_parse(sent):
    print tree
    #до прикладу,використовуємо граматику для речення,яке складається з 8 слів.

    sent_1 = "Ann looked at her boy in the garden".split()
rd_parser_1 = nltk.RecursiveDescentParser(grammar1)
for tree_1 in rd_parser_1.nbest_parse(sent_1):
    print tree_1
    # ми бачимо тут два дерева,отже, можемор зробити висновок, що це речення є структурно неоднозначним.
    
