# Veronika  Klantsak ALs-11

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
sent = 'Ron read a book'.split() # split my sentence
for t in rd_parser.nbest_parse(sent):
print t
# use graphical demonstration to see the grammar (top-down parsing)
nltk.app.rdparser()

# pislya modufikacii gramatuku mu bachumo, sho vidbyvaet'sya zacuklennya
# programmu na perwomy pravuli.Vono e rekyrsuvnum tome vurazhaet'sya samo
# cherez sebe i tomy analizator ne perexodut' do nastypnogo pravula.
