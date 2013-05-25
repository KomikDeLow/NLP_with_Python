# Maryna Ivaniv PRLs-11 Chapter 7, Ex.5
# Write a tag pattern to cover noun phrases that contain gerunds, e.g., 
# the/DT receiving/VBG end/NN, assistant/NN managing/VBG editor/NN.
# Add these patterns to the grammar, one per line.
# Test your work using some tagged sentences of your own devising.


import nltk
grammar = "NP: {<DT|NN>?<VBG><NN>}" # create a chunk parser.chunk determiner(DT)/noun(NN),gerund(VBG) and noun(NN)
sentence =[("The", "DT"), ("receiving", "VBG"), ("end", "NN"), ("," , ","), ("assistant", "NN"),
("managing", "VBG"), ("editor", "NN")] # create sentence with POS tags
cp = nltk.RegexpParser(grammar) # create a chunk parser test it on our example sentence
print cp.parse(sentence)

sentence =[("Feeling", "VBG"), ("gratitude", "NN"), ("and", "CC"), ("not", "RB"), ("expecting", "VBG"),
("it", "DT"), ("is", "VB"), ("like", "RB"), ("wrapping", "VBG"), ("presents", "NNS"),
("and", "CC"), ("not", "RB"), ("giving", "VBG"), ("it", "DT"), ("." , ".")]
cp = nltk.RegexpParser(grammar)
print cp.parse(sentence)# print parse
