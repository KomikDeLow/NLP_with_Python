# TODO
# accuracy of your chunk parser??
#

#Прокулевич К. ПРЛс-11, Розділ 7, Завдання 4
#the entire sentence is put into a single chunk, then excise the chinks
import nltk
grammar = r"""
      NP:          
      {<.*>+}                 #Chunk everything    
      }<VB|IN>+{              #Chink sequences of VB and IN 
      """
sentence=[("Every", "DT"), ("day", "NN"), ("Tom", "NNP"), ("goes", "VB"), ("to", "IN"), ("school", "NN")]
cp = nltk.RegexpParser(grammar)
print cp.parse(sentence)
from nltk.corpus import conll2000
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents)
