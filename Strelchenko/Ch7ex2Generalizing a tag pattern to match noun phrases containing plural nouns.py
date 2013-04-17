# TODO
# doc string
# "sentence" isn't natural language sentence

import nltk
sentence = [("many", "JJ"), ("researches", "NNS"),(",", ","), ("two", "CD"),("weeks", "NNS"),(",", ","), ("both", "DT"), ("new", "JJ"), ("positions", "NNS")]
grammar = "NP: {<DT|CD>?<JJ>*<NN.>}" # defining a grammar rule which indicates how sentence should be chunked
cp = nltk.RegexpParser(grammar) # creating a chunk parser
result = cp.parse(sentence) # # fulfilling it on sentence
print result
result.draw() # The figure shows the nouns phrases containing plural head nouns
