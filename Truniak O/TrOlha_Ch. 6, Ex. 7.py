# Presented by Olha Truniak, ALs-13
# Chapter 6, Ex. 7


# Carry out the following evaluation tasks for any of the chunkers you have developed
# earlier. (Note that most chunking corpora contain some internal inconsistencies,
# such that any reasonable rule-based approach will produce errors.)

import nltk
from nltk.corpus import conll2000
print conll2000.chunked_sents('train.txt', chunk_types=['PP'])[:100]
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('train.txt', chunk_types=['PP'])
another = cp.evaluate(test_sents)
""" Use the chunkscore.missed() and chunkscore.incorrect() methods to
identify the errors made by your chunker:"""
print len(another.missed())
print len(another.incorrect())
print another.missed() [123]

""" Compare the performance of my chunker to the baseline chunker in
the evaluation section of this chapter"""
print conll2000.chunked_sents('train.txt', chunk_types=['NP'])[:100]
print conll2000.chunked_sents('train.txt', chunk_types=['PP'])[:100]
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
print cp.evaluate(test_sents)

