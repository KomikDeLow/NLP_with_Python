#Olesya Mykhaulyk
#ALs-12
#chapter 7 ex 8
import nltk
grammar = r"""
	NP:
	   {<.*>+} #Chunk everything
	   }<VBD|IN>+{ #Chink sequences of VBD and IN
	""" 
sentence= [('the','DT'),('little','JJ'),('yellow','JJ'),('dog','NN'),
           ('barked','VBD'),('at','IN'),('the','DT'),('cat','NN')]
cp=nltk.RegexpParser(grammar)# we use grammar in order to create a chunk parser and test it
                            #on the sentence
print cp.parse(sentence)

from nltk.corpus import conll2000 
cp = nltk.RegexpParser(grammar)# using grammar, we create a chunk parser and test
                                #it on our sentence
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents) # display evaluation results
