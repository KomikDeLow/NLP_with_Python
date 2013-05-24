#Ivanna Kushniruk

""" Write one or more tag patterns to handle coordinated noun phrases, e.g.,
July/NNP and/CC August/NNP,
all/DT your/PRP$ managers/NNS and/CC supervisors/NNS,
company/NN courts/NNS and/CC adjudicators/NNS."""

import nltk
sentence = [("July", "NNP"), ("and", "CC"), ("August", "NNP"),(",", ","),
            ("all", "DT"), ("your", "PRP$"), ("managers", "NNS"),("and", "CC"),
            ("supervisors", "NNS"), ("company", "NN"),("courts", "NNS"),
            ("and", "CC"), ("adjudicators", "NNS")]
#define a grammar
grammar = r"""
	NP: {<DT><PRP\$><NN.><CC><NN.*>}
            {<NN.*>+<CC><NN.>}
	"""

cp = nltk.RegexpParser(grammar)#create a chunk parser
print cp.parse(sentence)#represent result
