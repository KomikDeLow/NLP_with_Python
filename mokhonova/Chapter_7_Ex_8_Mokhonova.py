#Chapter_7_Ex_8_Mokhonova
import nltk
grammar = r"""
	NP:
	   {<.*>+} #Chunk everything
	   }<VBD|IN>+{ #Chink sequences of VBD and IN
	""" 
sentence= [('the','DT'),('little','JJ'),('yellow','JJ'),('dog','NN'),
           ('barked','VBD'),('at','IN'),('the','DT'),('cat','NN')]
cp=nltk.RegexpParser(grammar)# vykorystovuju gramatyku dlya stvorennya chunk parser 
                            #i testuvannya jogo v rechenni
print cp.parse(sentence)

from nltk.corpus import conll2000 
cp = nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents) # vuvodzhu resul'tat
