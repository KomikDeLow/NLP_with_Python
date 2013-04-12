# Petrukha Tetiana Als-11
# Chapter_8, Ex_2

# With pen and paper, manually trace the execution of a recursive descent parser
# and a shift-reduce parser, for a CFG you have already seen, or one of your own devising.

import nltk
sent = ['I', 'started', 'project'] # create sentence
grammar1 = nltk.parse_cfg("""
S -> NP VP
NP -> "I"
VP -> V NP
V -> "started"
NP -> "project"
""")  # define a simple grammar
sent = "I started project".split()
rd_parser = nltk.RecursiveDescentParser(grammar1, trace = 3) 
result = rd_parser.parse(sent) # create a parser
result.draw() # print a graphic representation of tree
