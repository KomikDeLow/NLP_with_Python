# TODO
# You didn't inspect the missed and incorrect chunks only print len.
#


# Evaluating a chunker (on 100 sentenses from a chunked corpus) and displaying its mistakes
# Copiyng a chunker builded in task 3 (Chapter 7)

import nltk
from nltk.corpus import *
from nltk.chunk.util import *

testColl_Sents=conll2000.chunked_sents('test.txt',chunk_types=['PP'])[:100]

grammar = r"""
PP: {<IN>?<JJ|RB|TO>?<IN>?}
    {</><CC>}
"""
cp=nltk.RegexpParser(grammar)
print cp.evaluate(testColl_Sents)

chunkscore = ChunkScore()
text_to_chunk=conll2000.tagged_sents('test.txt')[:100]
chunked_text=[]
for sent1 in text_to_chunk:
    chunked_text.append(cp.parse(sent1))

chunkscore.score(testColl_Sents, chunked_text)
print 'Missed: ',len(chunkscore.missed())
print 'Incorrect: ', len(chunkscore.incorrect())

# I don't understand why there are so many mistakes, and incorect ones,=, and the accuracy is good...


