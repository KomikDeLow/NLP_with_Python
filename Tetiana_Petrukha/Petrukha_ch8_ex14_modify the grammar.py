# Petrukha Tetiana Als-11
# Chapter_8, Ex_14

# You can modify the grammar in the recursive descent parser demo by selecting
# Edit Grammar in the Edit menu. Change the first expansion production, namely
# NP -> Det N PP, to NP -> NP PP. Using the Step button, try to build a parse tree.
# What happens?

import nltk
sent = ['I', 'started', 'project'] # create sentence
grammar1 = nltk.parse_cfg("""
S -> NP VP
NP -> NP PP
NP -> "I"
VP -> V NP
V -> "started"
NP -> "project"
""")  # define a simple grammar
sent = "I started project".split()
rd_parser = nltk.RecursiveDescentParser(grammar1, trace = 3)
result = rd_parser.parse(sent) # create a parser
result.draw() # print a graphic representation of tree

# When you change current rule, the program looping on the step of parse

