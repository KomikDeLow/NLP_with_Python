# TODO
# I didn't see a shift-reduce parser
#
# Petrukha Tetiana Als-11
# Chapter_8, Ex_11

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
sr_parse = nltk.ShiftReduceParser(grammar1, trace = 2) 
result = sr_parse.parse(sent) # create a parser
result.draw() # print a graphic representation of tree
