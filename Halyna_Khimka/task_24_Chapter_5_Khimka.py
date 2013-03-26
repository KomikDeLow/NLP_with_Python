# fine but you created variable "sents" -  and didn't use.
#Halyna Khimka
# Chapter 5, Task 24
# How serious is the sparse data problem? Investigate the performance of n-gram
#taggers as n increases from 1 to 6. Tabulate the accuracy score. Estimate the training
#data required for these taggers, assuming a vocabulary size of 105 and a tagset size
#of 102.
# 
#  sents=brown.sents() why?
import nltk
from nltk.corpus import brown
sents=brown.sents()
tagged_sents=brown.tagged_sents()
train_sents=tagged_sents[:1000] # dani dlia trenuvannja
diap=[1,2,3,4,5,6] # diapazon zna4enj
for i in diap:
	t=nltk.NgramTagger(n=i, train=train_sents)
	print 'N=',i, 'Evaluation:', t.evaluate (tagged_sents[1000:1200])
