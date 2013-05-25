# Roman Borys PRLs-11
import nltk
#Setting grammar
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
rd_parser = nltk.RecursiveDescentParser(grammar1)# parser
sent = 'Mary saw a dog'.split()# creating sentence
for t in rd_parser.nbest_parse(sent):
    print t # results
sent = 'John ate a cat'.split() #changed sentence
for t in rd_parser.nbest_parse(sent):
	print t #results
sent = 'Bob saw a telescope'.split() #creating one more sentence
for t in rd_parser.nbest_parse(sent):
	print t
sent = 'Mary saw Bob with a cat'.split() #changing sentence
for t in rd_parser.nbest_parse(sent):
	print t

sent = 'Mary saw Bob with a cat in the park'.split() #adding new words
print t
