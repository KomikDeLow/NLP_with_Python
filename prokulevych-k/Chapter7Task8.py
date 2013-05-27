# fine
# TODO
# ..., merging, or splitting.
#
#Прокулевич К. ПРЛс-11б Розділ7 Задача8
#Develop a chunker using a regular expression–based chunk grammar RegexpChunk.
import nltk
grammar = r"""
NP:
   {<.*>+} # Chunk everything
   }<VBD|VBG|IN|TO|VB>+{ # Chink sequences of VBD,VBG,IN,TO and VB
"""
cp = nltk.RegexpParser(grammar)
sentence=[("Beyond", "IN"), ("providing", "VBG"), ("insights", "NNS"),("into", "IN"), ("heart", "NN"), ("and", "CC"), ("lung", "NN"), ("deseases", "NNS"),(",", ","), ("invention", "NN"), ("encouraged", "VBD"), ("doctors", "NNS"), ("to", "TO"), ("do", "VB"), ("objective", "JJ"), ("investigations", "NNS")]
print cp.parse(sentence)
from nltk.corpus import conll2000
cp = nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents)
#The IOB accuracy shows that more than half of the words are in NP chunk.
 
