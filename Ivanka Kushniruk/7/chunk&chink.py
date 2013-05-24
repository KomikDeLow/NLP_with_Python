#Ivanna Kushniruk
#7.4

import nltk
#define sentence
sentence = [("the", "DT"), ("little", "JJ"), ("girl","NN"),
            ("looked", "VBD"), ("at", "IN"), ("the", "DT"),
            ("cake", "NN")] 
#define grammar, at first chunk everything and then chink
grammar = r"""
    NP:
	{<.*>+} # chunk everything 
	}<VBD|IN>+{
	"""
cp = nltk.RegexpParser(grammar)  #create a chunk parser
result = cp.parse(sentence)    #present result
print result

