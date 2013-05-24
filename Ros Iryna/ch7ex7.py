#Iryna Ros, chapter7, exersise 7
# 
#We will create chunker, which is based on regular expressions,
#which is evaluated on 100 sentenses from chunked corpus and which
#finds noun phrases.For error identification we use chunkscore.missed()
#and chunkscore.incorrect() methods. Also we create and evaluate baseline chunker.
#
import nltk
from nltk.corpus import conll2000
grammar = "NP: {<DT|AT|>?<OD>?<JJ.*>*<N.*>+}" #grammar based on regular expressions rules
Chunker = nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])[100:200]
chunkscore = Chunker.evaluate(test_sents)
print 'Task A: Evaluation of Chunker on 100 sentences from a chunked corpus'
print chunkscore

#Error identification with help of chunkscore.missed() and chunkscore.incorrect() methods.
print 'Task B: Using chunkscore.missed() and chunkscore.incorrect() methods for identifying errors'
print 'Miised: ',chunkscore.missed()[:8]
print 'Incorect: ',chunkscore.incorrect()[:8]

# Comparing the performance of two chunkers my and baseline. 
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])[100:200]
print 'C: The performance of a baseline chunker: ',cp.evaluate(test_sents)
