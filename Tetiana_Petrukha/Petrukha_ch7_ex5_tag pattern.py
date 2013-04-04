# Petrukha Tetiana Als-11
# Chapter_7, Ex_5

# Write a tag pattern to cover noun phrases that contain gerunds, e.g., 
# the/DT receiving/VBG end/NN, assistant/NN managing/VBG editor/NN.
# Add these patterns to the grammar, one per line.
# Test your work using some tagged sentences of your own devising.

import nltk
grammar = r"""
NP: {<DT|NN>?<VBG><NN>}""" # create ragular expression
sentence =[("The", "DT"), ("receiving", "VBG"), ("end", "NN"), ("," , ","), ("assistant", "NN"),
("managing", "VBG"), ("editor", "NN")] # create sentence with POS tags
cp = nltk.RegexpParser(grammar) # create a chunk parser test it on our example sentence
print cp.parse(sentence) # print parse
sentence =[("This", "DT"), ("tactic", "JJ"), ("has", "VBZ"), ("proven", "VBN"), ("successful", "JJ"),
("for", "IN"), ("some", "DT"), ("," , ","), ("however", "RB"), ("most", "RBS"), ("people", "NNS"),
("do", "VBP"), ("not", "RB"), ("enjoy", "VB"), ("utilizing", "VBG"),("this", "DT"), ("technique", "NN"),
("or", "CC"), ("being", "VBG"), ("on", "IN"), ("the", "DT"), ("receiving", "VBG"), ("end", "NN"),
("on", "IN"), ("the", "DT"), ("tactic", "JJ"), ("." , ".")] # create sentence with POS tags
cp = nltk.RegexpParser(grammar) # create a chunk parser test it on our example sentence
print cp.parse(sentence) # print parse
