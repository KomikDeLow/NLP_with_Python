# TODO
# accuracy of your chunk parser??
#

#���������� �. ����-11, ����� 7, �������� 4
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
