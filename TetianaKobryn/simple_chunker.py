# Presented by Tetiana Kobryn

# Chapter 7, Ex. 3
# Pick one of the three chunk types in the CoNLL-2000 Chunking Corpus. Inspect
# the data and try to observe any patterns in the POS tag sequences that make up
# this kind of chunk. Develop a simple chunker using the regular expression chunker
# nltk.RegexpParser. Discuss any tag sequences that are difficult to chunk reliably.


import nltk
from nltk.corpus import conll2000
#defining a  grammar with a regular expression rule
grammar = "NP: {<DT>?<JJ>*<NN><POS>?<VBG>*<JJ>*<NN>*<NNS>*}"
#creating a chunk parser
new_chunk = nltk.RegexpParser(grammar)
#some example sentence
sentence = [("The", "DT"), ("new", "JJ"), ("line", "NN"), ("'s", "POS"),
            ("capacity", "NN"), ("to", "TO"), ("adversely", "RB"),
            ("affect", "VB"), ("the", "DT"), ("company", "NN"), ("'s", "POS"),
            ("existing", "VBG"), ("hot-dipped", "JJ"), ("galvanizing", "NN"),
            ("lines", "NNS")]

#testing a grammar on example sentence
result = new_chunk.parse(sentence)
print result

#evaluating created chunker on chunked sentences from conll2000 corpus
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print new_chunk.evaluate(test_sents)
