# Shylimova K. Al-13
# Chapter 6 task 4

import random
import nltk
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
stop = stopwords.words('english') + list(",.-!?`':;()")
documents = [(list(movie_reviews.words(fileid)), category)
	     for category in movie_reviews.categories()
	     for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
words = nltk.FreqDist(w.lower() for w in movie_reviews.words()
		      if not w in stop)

word_features = words.keys()[:300]
def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features[word] = (word in document_words)
	return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[400:], featuresets[:400]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
classifier.show_most_informative_features(30)
