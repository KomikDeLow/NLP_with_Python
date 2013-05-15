import nltk
# define a grammar
grammar = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park"
P -> "in" | "on" | "by" | "with"
""")
# parse the grammar with RecursiveDescentParser
rd_parser = nltk.RecursiveDescentParser(grammar)
# split my sentence
sent = 'Mary saw a dog'.split()
for t in rd_parser.nbest_parse(sent):
	print t
# use graphical demonstration to see the grammar (top-down parsing)
nltk.app.rdparser()
# parse the grammar with ShiftReduceParser
sr_parse = nltk.ShiftReduceParser(grammar)
sent = 'Mary saw a dog'.split()
print sr_parse.parse(sent)
# use graphical demonstration to see the grammar (bottom-up parsing)
nltk.app.srparser()
# check what productions are currently in the grammar
for p in grammar.productions(): print p
