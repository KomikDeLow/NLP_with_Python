#Halyna Khimka
#Chapter7.3
#SimpleChunker
#
"""
The first Chunk Parser based on regular expressions finds Noun Phrases in given sentence.
The result of passing is drawn.
It is given a testing data for parser and evaluation is made.

The second Chunk Parser is also based on regular expressions but it finds prepositional phrases.


"""
import nltk
from nltk.corpus import conll2000
from nltk.corpus import brown
sent=('The', 'AT'), ('largest', 'JJT'), ('hurdle', 'NN'), ('the', 'AT'), ('Republicans', 'NPS'), ('would', 'MD'), ('have', 'HV'), ('to', 'TO'), ('face', 'VB'), ('is', 'BEZ'), ('a', 'AT'), ('state', 'NN'), ('law', 'NN')
print 'Sent :',sent
grammar = "NP: {<DT|AT|>?<OD>?<JJ.*>*<N.*>+}"
cp = nltk.RegexpParser(grammar)
ParsedSent=cp.parse(sent)
print ParsedSent.draw()

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents)


test_sents1 = conll2000.chunked_sents('test.txt', chunk_types=['PP'])
grammar1=r"PP:{<IN><DT>?<OD>?<N.*|PR.*|VBG>+}"
cp1 = nltk.RegexpParser(grammar1)
print cp1.evaluate(test_sents1)
