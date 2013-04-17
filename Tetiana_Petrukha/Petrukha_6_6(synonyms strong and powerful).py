# fine but I don't see you 
#
# TODO
# Comments?
# accuracy is lowest?

# Petrukha Tetiana Als-11
# Chapter_6, Ex_6

# The synonyms strong and powerful pattern differently
# (try combining them with chip and sales).
# What features are relevant in this distinction?
# Build a classifier that predicts when each word should be used.

import nltk
from nltk.corpus import brown
featureset=[] # creating an empty list for the features
context={}
for tagged_sent in brown.tagged_sents():
	for (w1,t1), (w2,t2) in nltk.bigrams(tagged_sent): #  In code-two-word-phrase we consider each two-word window in the sentence 
		 if t1.startswith('JJ') and w1 == 'strong': #  check if they meet our criterion
			 context[w2]=t2
			 featureset.append((context,w1))
			 context={}
		 elif t1.startswith('JJ') and w1 == 'powerful':
			 context[w2]=t2
			 featureset.append((context,w1))
			 context={}
print featureset[100]
print featureset[150]
print featureset[160]
size = int(len(featureset) * 0.01) # choose data size for testing
train_set, test_set = featureset[size:], featureset[:size] # divide data for train and test
classifier = nltk.NaiveBayesClassifier.train(train_set) # create a classifier
print nltk.classify.accuracy(classifier, test_set) # evaluate the accuracy of the work
print classifier.classify({'sales':'NNS'})
print classifier.classify({'chip':'NN'})
print classifier.classify({'body':'NN'})
print classifier.classify({'factor':'NN'})
