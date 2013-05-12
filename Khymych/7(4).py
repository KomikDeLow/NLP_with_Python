import nltk
grammar= r"""
Np:{<.*>+}
}<VBD|IN>+{
"""               #Define a simple grammar: {<.*>+} - chunk everything. }<VBD|IN>+{ - Chink sequences of VBD and IN
sentence=[("The", "DT"), ("Little", "JJ"), ("Red", "JJ"), ("Cap", "NN"),
          ("walked", "VBD"), ("in", "IN"), ("the", "DT"), ("forest", "NN")] #Sentences that should be chunked.
chunk_parser=nltk.RegexpParser(grammar) #Create a chunk parser
print chunk_parser.parse(sentence) #The result is a tree, which we can print
from nltk.corpus import conll2000 #Access the data of the CoNLL-2000 Chunking Corpus. The corpus contains 270k words of 
                                  #Wall Street Journal text, divided into “train” and “test” portions, annotated with 
								  #part-of-speech tags and chunk tags in the IOB format.
chunk_parser=nltk.RegexpParser(grammar) #Once more create a chunk parser
test_sents=conll2000.chunked_sents('test.txt', chunk_types=['NP']) #We are interested in the NP chunks right now.  
                                                                   #So we can use the chunk_types argument to select them.
print chunk_parser.evaluate(test_sents) #Evaluate chunker on the data for testing
