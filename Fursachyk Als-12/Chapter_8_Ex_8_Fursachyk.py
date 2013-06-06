#Chapter_8_Ex_8_Fursachyk
import nltk
#opysujemo prostu gramatyku
grammar1 = nltk.parse_cfg("""
#S -> NP VP
#VP -> V NP | V NP PP
#PP -> P NP
#V -> "saw" | "ate" | "walked"
#NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
#Det -> "a" | "an" | "the" | "my"
#N -> "man" | "dog" | "cat" | "telescope" | "park"
#P -> "in" | "on" | "by" | "with"
#""")
rd_parser = nltk.RecursiveDescentParser(grammar1)#programa syntaksychnogo analizu
sent = 'Mary saw a dog'.split()#stvorjuemo rechennya
for t in rd_parser.nbest_parse(sent):
	print t #vyvodymo syntaksychnyj analiz
	sent = 'John ate a cat'.split() #zminjuemo rechennya

for t in rd_parser.nbest_parse(sent):
	print t 

sent = 'Bob saw a telescope'.split() #stvorjuemo shche odne rechennya
for t in rd_parser.nbest_parse(sent):
  print t

sent = 'Mary saw Bob with a cat'.split() #zminjuemo rechennya
for t in rd_parser.nbest_parse(sent):
	print t

sent = 'Mary saw Bob with a cat in the park'.split() #dodaemo novi slova
for t in rd_parser.nbest_parse(sent):
	print t

