# Presented by Olha Truniak, ALs-13
# Chapter 7, Ex.5

# Write a tag pattern to cover noun phrases that contain gerunds, e.g., the/DT
# receiving/VBG end/NN, assistant/NN managing/VBG editor/NN. Add these patterns
# to the grammar, one per line. Test your work using some tagged sentences of your
# own devising.

import nltk
# Make simple noun phrase chunker
grammar = r"""
        NP: {<DT|NN>?<VBG><NN>}""" # chunk determiner/possessive, verb(gerund) and noun
sentence = [("the", "DT"), ("receiving", "VBG"), ("end", "NN"),
           (",", "."), ("assistant", "NN"), ("managing", "VBG"), ("editor", "NN")]
cp = nltk.RegexpParser(grammar)
print cp.parse(sentence) # run the chunker on this input
sentence = [("John", "NNP"), ("thinks", "VBZ"), ("Mary", "NN"),
           ("saw", "VBD"), ("the", "DT"), ("cat", "NN"), ("sit", "VB"),
           ("on", "IN"), ("the", "DT"), ("mat", "NN")]
cp = nltk.RegexpParser(grammar)
print cp.parse(sentence)# run the chunker on this input
