# Iryna Brykailo, ALs-13

import nltk
grammar = r"""
        NP: {<DT|NN>?<VBG><NN>}""" # Creating noun phrase chunker
sentence = [("the", "DT"), ("receiving", "VBG"), ("end", "NN"),
           (",", "."), ("assistant", "NN"), ("managing", "VBG"), ("editor", "NN")]
cp = nltk.RegexpParser(grammar)
print cp.parse(sentence) # Printing the chunker
sentence = [("Lisa", "NNP"), ("thinks", "VBZ"), ("Andrew", "NN"),
           ("saw", "VBD"), ("the", "DT"), ("bird", "NN"), ("sit", "VB"),
           ("on", "IN"), ("the", "DT"), ("branch", "NN")]
cp = nltk.RegexpParser(grammar)
print cp.parse(sentence) # Run the chunker on the example
