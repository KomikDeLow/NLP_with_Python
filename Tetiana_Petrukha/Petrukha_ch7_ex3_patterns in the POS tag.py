# Petrukha Tetiana Als-11
# Chapter_7, Ex_3

# Pick one of the three chunk types in the CoNLL-2000 Chunking Corpus.
# Inspect the data and try to observe any patterns in the POS tag sequences 
# that make up this kind of chunk.
# Develop a simple chunker using the regular expression chunker nltk.RegexpParser.
# Discuss any tag sequences that are difficult to chunk reliably.

import nltk, re, pprint
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"),
            ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")] # create sentence with POS tags
grammar = "NP: {<DT>?<JJ>*<NN>}" # create ragular expression
cp = nltk.RegexpParser(grammar) # create a chunk parser
result = cp.parse(sentence) # test chunk parser on my sentence
print result # print result
from nltk.corpus import conll2000 # import conll2000 corpus for making evaluation
print conll2000.chunked_sents('train.txt', chunk_types=['PP'])[49]
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['PP'])# get training and testing data
print cp.evaluate(test_sents) # the chunker got decent results and is ready to use

grammar = r"PP: {<[INNN].*>+}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
grammar = r"PP: {<IN><DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
grammar = r"PP: {<NN>?<VB.*>+}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
grammar = r"PP: {<JJ>?<IN>?<TO>?}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
grammar = r"PP: {<VB.*>?<NN.*>*<DT>*}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
