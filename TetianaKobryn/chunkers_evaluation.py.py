# fine

# Presented by Tetiana Kobryn

# Chapter 7, Ex. 7

# Carry out the following evaluation tasks for any of the chunkers you have
# developed earlier.
# a.
#Evaluate your chunker on 100 sentences from a chunked corpus, and report
#the precision, recall, and F-measure.
# b. 
#Use the chunkscore.missed() and chunkscore.incorrect() methods to identify
#the errors made by your chunker. Discuss.
# c. 
#Compare the performance of your chunker to the baseline chunker discussed
#in the evaluation section of this chapter.



import nltk
from nltk.corpus import conll2000
#defining a grammar with a regular expression rule
grammar = "NP: {<DT>?<JJ>*<NN><POS>?<VBG>*<JJ>*<NN>*<NNS>*}"
#creating a chunk parser
new_chunk = nltk.RegexpParser(grammar)

#####
# a.
#####
print "a)"
#evaluating created chunker on chunked sentences from conll2000 corpus
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])[:100]
chunkscore = new_chunk.evaluate(test_sents)
print chunkscore

#####
# b.
#####
print "b)"
#identifying the errors made by new chunker
print chunkscore.missed()[:10]
print chunkscore.incorrect()[:10]
#####
# c.
#####
print "c)"
#creating and evaluating the baseline chunker
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])[:100]
print cp.evaluate(test_sents)
print """The performance of created chunker is better than the performance of
the baseline chunker, as in the new chunker some grammar is defined"""
