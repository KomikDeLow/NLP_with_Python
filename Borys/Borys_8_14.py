import nltk
sent = ['I', 'loved', 'rain'] #creating sentence
grammar1 = nltk.parse_cfg("""
#S -> NP VP
#NP -> DET N PP
#NP -> "I"
#VP -> V NP
#V -> "loved"
#NP -> "rain"
#""") #setting grammar
sent = "I loved rain".split()
rd_parser = nltk.RecursiveDescentParser(grammar1, trace = 3)
result = rd_parser.parse(sent) #showing results
result.draw()
grammar1 = nltk.parse_cfg("""
S -> NP VP
NP -> NP PP
NP -> "I"
VP -> V NP
V -> "loved"
NP -> "rain"
""")
sent = "I loved rain".split()
rd_parser = nltk.RecursiveDescentParser(grammar1, trace = 3) #parsing
result = rd_parser.parse(sent)

