# TODO
# Is the value of variable sentence a natural language sentence
#

import nltk
from nltk.corpus import conll2000 
sentence = [("A","DT"), ("dark","JJ"), ("red","JJ"), ("car","NN"), ("came","VDT"),("to","IN"), ("a","DT"), ("stop","NN"), ("in","IN"), ("front","NN"), ("of","IN"), ("the", "DT"), ("Flynn-Fletcher","JJ"), ("residence","NN"), ("that","WDT"), ("same", "JJ"), ("evening","NN"), (",",","), ("in", "IN"), ("another", "DT"), ("demension","NN"), (".",".")]
grammar = "NP: {<DT>?<JJ>*<VB>}" # building a grammar rule
cp= nltk.RegexpParser(grammar) # creating a chunk parser
result = cp.parse(sentence)
print result
result.draw() # Using regular expressions, this rule works when chunker finds determinant, after which comes an unlimited number of adjectives, but in the end comes a noun.
