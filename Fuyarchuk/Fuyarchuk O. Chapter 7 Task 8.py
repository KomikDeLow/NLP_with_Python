# TODO
# ...merging, or splitting ?

# Fuyarchuk O. Chapter 7. Task 8

import nltk
grammar = r"""
	NP:
	   {<.*>+} #Chunk everything
	   }<VBD|IN|VBN>+{ #Chink sequences of VBD,IN,VBN
	""" 
sentence= [("Although","IN"),("the","DT"),("old","JJ"),("regime","NN"),
           ("was","VBD"),("driven","VBN"),("out","IN"),("new","JJ"),("ideas","NNS"),
           ("were","VBD"),("explored","VBD"),("which","DT"),("emphasized","VBD"),
           ("observation","NN"),("and","IN"),("reasons","NNS")]
cp=nltk.RegexpParser(grammar)# Using grammar create a chunk parser and test it
                            #on our sentence
print cp.parse(sentence)
from nltk.corpus import conll2000 # import conll2000 corpus
cp = nltk.RegexpParser(grammar)# using grammar create a chunk parser and test
                                #it on our sentence
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents) # print evaluation result
