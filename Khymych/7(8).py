import nltk
from nltk.corpus import conll2000 #Access the data of the CoNLL-2000 Chunking Corpus. The corpus contains 270k words of 
                                  #Wall Street Journal text, divided into “train” and “test” portions, annotated with 
				                  #part-of-speech tags and chunk tags in the IOB format.
cp = nltk.RegexpParser("") #Create the trivial chunk parser that creates no chunks
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['PP'])
print cp.evaluate(test_sents)
#The IOB tag accuracy indicates that near 90% of the words are tagged with 0.
#However, since our tagger did not find any chunks, its precision, recall, and F-measure are all zero.
grammar = r"""
PP:
{<.*>+}                       
}<NN|TO|PRP$|JJ|CC|NN.|VB.>+{
"""  #{<.*>+} - Chunk everything. }<NN|TO|PRP$|JJ|CC|NN.|VB.>+{ - Chink sequences of NN,TO,PRP$,JJ,CC,NNS, NNP,VBZ
sentence= [("In", "IN"),("addition", "NN"),("to", "TO"),("his", "PRP$"),("previous", "JJ"),("real-estate", "NN"),
           ("investment", "NN"),("and", "CC"),("asset-management", "NN"),("duties", "NNS"),("Mr.", "NNP"),("Meador", "NNP"),
           ("takes", "VBZ"),("responsibility", "NN"),("for", "IN"),("development", "NN"),("and", "CC"),("property", "NN"),
           ("management", "NN")] #Sentence that should be chunked.
chunk_parser=nltk.RegexpParser(grammar) #Create a chunk parser
print chunk_parser.parse(sentence) #Test chunk_parser on our sentence. The result is a tree, which we can print
chunk_parser = nltk.RegexpParser(grammar)#Once more create a chunk parser
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['PP'])#We are interested in the PP chunks right now.  
                                                                    #So we can use the chunk_types argument to select them.
print chunk_parser.evaluate(test_sents) #Evaluate chunker on the data for testing
                                        #This approach achieves decent results.
