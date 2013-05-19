# Presented by Olha Truniak, ALs-13
# Chapter 6, Ex. 4

# Using the movie review document classifier discussed in this chapter, generate
# a list of the 30 features that the classifier finds to be most informative. Can you
# explain why these particular features are informative? Do you find any of them
# surprising?

import nltk
# I constructed a list of documents,labeled with the appropriate categories.
# I've chosen the Movie Reviews Corpus, which categorizes each review as
# positive or negative
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
	     for category in movie_reviews.categories()
	     for fileid in movie_reviews.fileids(category)]
# I defined a feature extractor for documents, so the classifier will know
# which aspects of the data
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words()) # A feature extractor for document classification, whose features indicate whether or not
# individual words are present in a given document.
word_features = all_words.keys()[:2000]
def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features
# Training and testing a classifier for document classification
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier.show_most_informative_features(30) # we can use show_most_informative_features()to find out which features
# the classifier found to be most informative
print
