#Change the first expansion production, namely
#NP -> Det N PP, to NP -> NP PP. Using the Step button,
#try to build a parse tree.

import nltk
grammar = nltk.parse_cfg("""  # define a grammar
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "read" | "saw" | "ate"
NP -> "Brad" | "Ron" | "Karla" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "book" | "dog" | "sandwitch" | "cup" | "park"
P -> "in" | "on" | "by" | "with"
""")
# parse the grammar with RecursiveDescentParser
rd_parser = nltk.RecursiveDescentParser(grammar)
sent = 'Ron read a book'.split()
for t in rd_parser.nbest_parse(sent):
    print t
nltk.app.rdparser()
#rezul'tat zacyklennja na pershomu pravyli, bo vono je rekursyvnym
