# Shylimova K. Al-13
# Chapter 6 task 8

import random
import nltk
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet

stop = stopwords.words('english') + list(",.-!?`':;()")
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words() 
                      if not w in stop)
word_features = all_words.keys()[:300]
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features[word] = (word in document_words)
    return features
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[400:], featuresets[:400]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print "Classifier accuracy without synsets: ", nltk.classify.accuracy(classifier, test_set)
print "Features count: ", len(word_features)
for word in all_words.keys()[:300]:
    if all_words[word] < all_words[all_words.keys()[200]]:
        for synset in wordnet.synsets(word):
            for hypernyms in synset.hypernyms():
                for l_name in hypernyms.lemma_names:
                    if (l_name not in word_features):
                        word_features.append(l_name)
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[400:], featuresets[:400]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print "Classifier accuracy with synsets: ", nltk.classify.accuracy(classifier, test_set)
print "Features count: ", len(word_features)
