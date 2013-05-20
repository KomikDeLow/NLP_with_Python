#Presented by Tkachuk Iryna

#7_6. Write one or more tag patterns to handle coordinated noun phrases, e.g.,
#July/NNP and/CC August/NNP, all/DT your/PRP$ managers/NNS and/CC supervisors/NNS
#, company/NN courts/NNS and/CC adjudicators/NNS.

import nltk
#define a  grammar with a regular expression rules
grammar = r"""
	NP: {<DT><PRP\$><NN.>+<CC>*<NN.*>+}
	{<NN.>+<CC>*<NN.>+}
	"""
#some sentence for testing parser
sentence = [("July", "NNP"), ("and", "CC"), ("August", "NNP"),(",", ","),
            ("all", "DT"), ("your", "PRP$"), ("managers", "NNS"),("and", "CC"),
            ("supervisors", "NNS"), ("company", "NN"),("courts", "NNS"),
            ("and", "CC"), ("adjudicators", "NNS")]

cp = nltk.RegexpParser(grammar)#create a chunk parser
print cp.parse(sentence)#represent result
