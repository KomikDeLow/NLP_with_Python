# TODO
# Comments?
# The style of program is bad. Four nested for loops !
# I didn't understand your program

# Petrukha Tetiana Als-11
# Chapter_6, ex_8

# Using the WordNet lexicon, augment the movie review document classifier presented
# in this chapter to use features that generalize the words that appear in a document,
# making it more likely that they will match words found in the training data.

import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
documents = [(list(movie_reviews.words(fileid)), category) # construct a list of documents, labeled with the appropriate categories
	     for category in movie_reviews.categories() # Iterate on all review categories.
	     for fileid in movie_reviews.fileids(category)] # For each category iterate on all reviews.
random.shuffle(documents) # Mix documents.
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words()) # Get all words from movie review.
word_features = all_words.keys()[:400] # constructing a list of the 400 most frequent words.
print len (word_features)
def document_features(document): # define a feature extractor
	document_words = set(document) #compute the set of all words in a document
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

#Training and testing a classifier for document classification:
featuresets = [(document_features(d), c) for (d,c) in documents]
size = int(len(featuresets) * 0.01)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
updated_word_features = set(word_features[:])  # Update the list of most frequent words.
for word in all_words.keys()[:500]:
        for synset in wn.synsets(word):
                for hypernym in synset.hypernyms():
                        for l_name in hypernym.lemma_names:
                                if l_name in word_features and word not in updated_word_features: 
                                        updated_word_features.add(word) 
			    
print len(updated_word_features)
featuresets = [(document_features(d), c) for (d,c) in documents]
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set) 
print nltk.classify.accuracy(classifier, test_set) # Evaluate accuracy on updated set.
