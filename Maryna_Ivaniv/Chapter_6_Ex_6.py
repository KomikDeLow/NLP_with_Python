#Maryna Ivaniv PRLs-11 Chapter 6 Ex.6
#The synonyms strong and powerful pattern differently (try combining them with
#chip and sales). What features are relevant in this
#distinction? Build a classifier that
#predicts when each word should be used.

import nltk
from nltk.corpus import brown
featureset = []# creating an empty list for the features
context={}
for tagged_sent in brown.tagged_sents():
	for (w1,t1),(w2,t2) in nltk.bigrams(tagged_sent):
		if t1.startswith('JJ') and w1 =='strong': #  check if they meet our criterion
			context[w2]=t2
			featureset.append((context,w1))
			context={}
		if t1.startswith ('JJ') and w1 =='powerful':
			 context [w2] =t2
			 featureset.append((context,w1))
			 context={}

			 
print featureset[100]
print featureset[150]
print featureset[160]
size = int(len(featureset) * 0.01) # choose data size for testing
train_set, test_set = featureset[size:], featureset[:size] # divide data for train and test
classifier = nltk.NaiveBayesClassifier.train(train_set)# create a classifier
print nltk.classify.accuracy(classifier, test_set)# evaluate the accuracy of the work
