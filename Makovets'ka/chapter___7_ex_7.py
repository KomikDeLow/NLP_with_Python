#Evaluate your chunker on 100 sentences from a chunked corpus
#report the precision, recall, and F-measure.
#Use the chunkscore.missed() and chunkscore.incorrect()

import nltk
from nltk.corpus import conll2000
grammar = "NP: {<DT|AT|>?<OD>?<JJ.*>*<N.*>+}" ##grammar based on regular expressions rules
Chunker = nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])[100:200] ##Evaluation of Chunker on 100 sentences from a chunked corpus
chunkscore = Chunker.evaluate(test_sents)
print 'Task A: Evaluation of Chunker on 100 sentences from a chunked corpus'
print chunkscore
print 'Task B: Using chunkscore.missed() and chunkscore.incorrect() methods for identifying errors'
print 'Miised: ',chunkscore.missed()[:10]
print 'Incorect: ',chunkscore.incorrect()[:10]
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])[100:200]
print 'C: The performance of a baseline chunker: ',cp.evaluate(test_sents)
