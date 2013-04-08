# TODO
# What is accuracy of your parser?

#Komar Mariia Als-11
#Chapter_7, Ex_8
#Develop a chunker for one of the chunk types in the CoNLL Chunking Corpus
#using a regular expression–based chunk grammar RegexpChunk. Use any combination
#of rules for chunking, chinking, merging, or splitting.

import nltk
grammar=""" # Create grammar  
         NP:
         {<DT>?<JJ>*<NN>*<NNS>*} #Chunk sequences of DT, JJ, NN, NNS
         }<VBP|IN>+{             #Chink sequences of VBD and IN   
         """
cp= nltk.RegexpParser(grammar) #create a chunk parser test it on our example sentence
sentence=[('Small', 'JJ'), ('beautiful', 'JJ'), ('cats', 'NNS'), ('stay', 'VBP'), ('on', 'IN'), ('the', 'DT'), ('yard', 'NN'), ('and', 'CC'), ('look', 'VBP'), ('on', 'IN'), ('the', 'DT'), ('blue', 'JJ'), ('sky', 'NN')]#test chunk parser on my sentence
print cp.parse(sentence)#print result

from nltk.corpus import conll2000 #import conll2000 corpus for making evaluation
cp = nltk.RegexpParser(grammar) #create a chunk parser test it on our example sentence
test_sents = nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=('NP',))
print  'Accuracy=', nltk.chunk.accuracy(cp, test_sents) #print evaluation

