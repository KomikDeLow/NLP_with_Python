# Prizvuszcze / Grypa

import nltk
sentence = [("Sumsung", "NNP"), ("is", "VBZ"), ("the", "DT"),
("leader", "NN"), ("in", "IN"), ("mobile", "JJ"), ("technology", "NN"), ("with", "IN"),("In-line", "JJ"), ("combination", "NN"), ("processes", "NNS"), ("for", "IN"), ("the", "DT"),("label", "NN"), ("industry", "NN"),  ("one", "CD"), ("of", "IN"), ("the", "DT"), ("fastest", "JJS"),("developing", "VBG"), ("trends", "NNS"), ("today", "NN] 
grammar = r""" ## grammar
NP:
	{<.*>+}   ##Chunk everything
	}<VBD|IN|CC|IN|MD|RB|RBR|RP|SYM|TO|UH|VB|VBD|VBG|VBN|VBP|VBZ|WRB>+{
	"""
cp = nltk.RegexpParser(grammar)  #using that grammar we create a chunk parser
result = cp.parse(sentence)      # test it on our example sentence





