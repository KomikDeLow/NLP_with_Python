# Komar Mariia Als-11
#Chapter5_ Ex_24
#How serious is the sparse data problem?
#Investigate the performance of n-gram taggers as n increases from 1 to 6.
#Tabulate the accuracy score.
#Estimate the training data required for these taggers, assuming a vocabulary size of 105 and a tagset size
#of 102.
# 
#The sparse data problem is serious.
#N-gram taggers can be defined for large values of n, but once n is larger than
#3, we usually encounter the sparse data problem;even with a large quantity of
#training data, we see only a tiny fraction of possible contexts.

import nltk
from nltk.corpus import brown
tagged_sents=brown.tagged_sents()
train_sents=tagged_sents # data for training
for i in range (1,7): # range= from 1 to 6
	n_grams = nltk.NgramTagger (i, nltk.corpus.brown.tagged_sents()[:1000])
	print  'N_gram, N=',i, n_grams.evaluate(nltk.corpus.brown.tagged_sents()[1000:1200])
