# TODO
# unexpected indent!!!
#

# Uliana Chubko
import nltk, re, pprint
 sentence = [("Many","JJ"), ("researchers","NNS"), ("developed","VBD "), ("both","DT"),
	     ("new","JJ"), ("positions","NNS"), ("two","CD"), ("weeks","NNS"), ("ago","RB")]# create sentence
 grammar = "NP: {<DT>*<CD>*<JJ>*<NN.*>+}"# create regular expressions
 cp = nltk.RegexpParser(grammar)# create a chunk parser test in our sentence
 result = cp.parse(sentence)# create a chunk parser test in my own sentence
 print result# print results
