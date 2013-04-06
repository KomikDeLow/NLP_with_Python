# TODO
# Comments?

# Petrukha Tetiana Als-11
# Chapter_6, Ex_4

# Using the movie review document classifier discussed in this chapter, generate
# a list of the 30 features that the classifier finds to be most informative.
# Can you explain why these particular features are informative?
# Do you find any of them surprising?

import nltk
from nltk.corpus import movie_reviews # import movie_reviews corpus
documents=[(list(movie_reviews.words(fileid)),category)
	   for category in movie_reviews.categories()
	   for fileid in movie_reviews.fileids(category)]
# construct a list of documents, labeled with the appropriate categories.
import random
random.shuffle(documents) # shuffle positive and negative features
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features=all_words.keys()[:2000]
def document_features(document): # take document
	document_words=set(document) # take the word of this document
	features={} # look for features
	for word in word_features:
		features['contains(%s)' %word]=(word in document_words) # check is the word contained in the document or not
	return features
    
featuresets=[(document_features(d),c) for (d,c) in documents]
train_set, test_set=featuresets[100:],featuresets[:100] # divide data for train and test
classifier=nltk.NaiveBayesClassifier.train(train_set) # train classifier
print nltk.classify.accuracy(classifier,test_set) # assess the accuracy of his work
print classifier.show_most_informative_features(30) # print a list of the 30 features that the classifier finds to be most informative
