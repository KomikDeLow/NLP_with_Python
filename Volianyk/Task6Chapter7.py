

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
#create a chunk parser
cp = nltk.RegexpParser(grammar)
#represent result
print cp.parse(sentence)
