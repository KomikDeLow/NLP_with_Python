#Iryna Ros, PRLs-11, chapter 5 exersise 24
#
#It is an investigation of the performance of n-gram taggers, and how n increases
#from 1 to 6. Also assuming a tagset size of 102 and a vocabulary size of 105.
#We tabulate the accuracy score.
#WE have sparse data problem which can happen when we use N-gram Taggers. With the help 
#of tagger context we find the correct  tag. But when N is larger, the context is more specific. 
#Unknown word would'nt be tagged.
#The increase of the amount of training data would't solve the problem.
#Thus the sparse data problem is one of the most important in NLP.
#
import nltk
from nltk.corpus import brown
tagged_sents=brown.tagged_sents()
train_sents=tagged_sents[:1000] 
diap=[1,2,3,4,5,6] # diapazon znachen
for i in diap:
	t=nltk.NgramTagger(n=i, train=train_sents)
	print 'N=',i, 'Evaluation:', t.evaluate (tagged_sents[1000:1200])
