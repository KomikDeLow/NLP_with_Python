# Valerii Androshchuk APL(s)-13
# Chapter 6, Task 4
# Generate a list of 30 features that the classifire finds
# the most informative. Do you find any of them surprising?
import nltk
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
	     for category in movie_reviews.categories()
	      for fileid in movie_reviews.fileids(category)]
                # Feature extraction determination.
words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = words.keys()[:500]
def document_features(document):
	document_w = set(document)
	features = {}
	for word in word_features:
		features[word] = (word in document_w)
		return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[400:], featuresets[:400]
classifier = nltk.NaiveBayesClassifier.train(train_set)
# Setting classifier.
print nltk.classify.accuracy(classifier, test_set)
classifier.show_most_informative_features(30)

#Nothing surprising.
