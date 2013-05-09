# Daria Morozova 
# Chapter 7 Ex.3
# I added the evaluation of my chunker


import nltk 
from nltk.corpus import conll2000   # importing CoNLL-2000 Chunking corpus
print conll2000.chunked_sents('train.txt', chunk_types=['NP'])[23] # read the 24 sentence of the train portion of the corpus
train_sents= conll2000.chunked_sents('train.txt', chunk_types=['NP'])[23] 
test_sents=conll2000.chunked_sents('test.txt', chunk_types=['NP'])
grammar = "NP: {<DT>?<JJ>*<NN>}" #creating a rule for the grammar
cp = nltk.RegexpParser(grammar)  #I create a chunk parser using a grammar
print cp.evaluate(test_sents)    #evaluate my chunker
