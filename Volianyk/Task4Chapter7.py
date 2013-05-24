
import nltk
grammar= r"""
         Np:{<.*>+}
         }<VBD|IN>+{
         """
# define a simple grammar: {<.*>+} - chunk everything. }<VBD|IN>+{ - Chink sequences of VBD and IN
sentence=[("The", "DT"), ("Little", "JJ"), ("Red", "JJ"), ("Cap", "NN"),
          ("walked", "VBD"), ("in", "IN"), ("the", "DT"), ("forest", "NN")] #Sentences that should be chunked.
# create a chunk parser
chunk_parser=nltk.RegexpParser(grammar)
# print results 
print chunk_parser.parse(sentence)
# access the data of the CoNLL-2000 Chunking Corpus. The corpus contains 270k words of
# Wall Street Journal text, annotated with part-of-speech tags and chunk tags in the IOB format.
from nltk.corpus import conll2000
# once more create a chunk parser
chunk_parser=nltk.RegexpParser(grammar)
# we are interested in the NP chunks right now.  
# so we can use the chunk_types argument to select them.
test_sents=conll2000.chunked_sents('test.txt', chunk_types=['NP'])
# evaluate chunker on the data for testing
print chunk_parser.evaluate(test_sents)
