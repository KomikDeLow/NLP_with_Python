import nltk
from nltk.corpus import conll2000
grammar = r"""
        NP: {<DT|NN>?<VBG><NN>}""" # Creating noun phrase chunker
Chunker = nltk.RegexpParser(grammar)# Chunker
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])[100:200]
chunkscore = Chunker.evaluate(test_sents) # Evaluating the chunk from the chunkrd corpus
print chunkscore
print 'Missed: ',chunkscore.missed()[:8] # Using chunkscore.missed and chunkscore.incorrect
print 'Incorrect: ',chunkscore.incorrect()[:8] #  to identify the errors made by my chunker
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])[100:200] # Comparing the performance of my chunker
print cp.evaluate(test_sents) # to the baseline chunker

# After Comparing the performance of my chunker
# to the baseline chunker I marked, that:
# IOB-Accuracy didn't changed,Precision,Recall and F-Measure care different(0).
# Methods chunkscore.missed and chunkscore.incorrect helped me to identify the errors made by my chunker.