#Halyna Khimka
# Chapter 7.7
# ChunkersEvaluation
#
"""
This program creates chunker which finds noun phrases.
the chunker is based on regular expressions.
The chunker is evaluated on 100 sentences from a chunked corpus.
Also chunkscore.missed() and chunkscore.incorrect() methods are used to identify errors.
The baseline chunker also is created and evaluated.
The performance of beseline chunker is much lower the the performance of my chunker.
"""
import nltk
from nltk.corpus import conll2000
grammar = "NP: {<DT|AT|>?<OD>?<JJ.*>*<N.*>+}" #grammar based on regular expressions rules
Chunker = nltk.RegexpParser(grammar)# my parser

#Evaluation of Chunker on 100 sentences from a chunked corpus
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])[100:200]
chunkscore = Chunker.evaluate(test_sents)
print 'Task A: Evaluation of Chunker on 100 sentences from a chunked corpus'
print chunkscore

#Use the chunkscore.missed() and chunkscore.incorrect() methods to identify
#the errors made by your chunker.
print 'Task B: Using chunkscore.missed() and chunkscore.incorrect() methods for identifying errors'
print 'Miised: ',chunkscore.missed()[:8]
print 'Incorect: ',chunkscore.incorrect()[:8]

# Comparing the performance of my chunker to the baseline chunker
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])[100:200]
print 'C: The performance of a baseline chunker: ',cp.evaluate(test_sents)
