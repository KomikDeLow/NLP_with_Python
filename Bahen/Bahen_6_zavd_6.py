# TODO
# Comments?
# How does your program work?
# Plagiarism!
#
#Bahen Diana, PRLs-11, Chapter 6, Exercise 6

import nltk
from nltk.corpus import brown
featureset=[]
context={}
for tagged_sent in brown.tagged_sents():
	for (w1,t1), (w2,t2) in nltk.bigrams(tagged_sent):
		 if t1.startswith('JJ') and w1 == 'strong':
			 context[w2]=t2
			 featureset.append((context,w1))
			 context={}
		 elif t1.startswith('JJ') and w1 == 'powerful':
			 context[w2]=t2
			 featureset.append((context,w1))
			 context={}
print featureset[100]
print featureset[125]
print featureset[150]
size = int(len(featureset) * 0.1)
train_set, test_set = featureset[size:], featureset[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
print classifier.classify({'sales':'NNS'})
print classifier.classify({'chip':'NN'})
print classifier.classify({'body':'NN'})
print classifier.classify({'factor':'NN'})
