# Presented by Olha Truniak, ALs-13
# Chapter 6, Ex.2

import nltk
# Start with preparing a list of examples and corresponding class labels
from nltk.corpus import names
names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])
# I’ll start by just looking at the last letter and some suffixes of a given name.
def gender_features(name):
        features = {}
        features["lastletter"] = name[-1].lower()
        features["suffix1"] = name[-2:].lower()
        features["suffix2"] = name[-4:].lower()
        features["suffix3"] = name[-6:].lower()
        return features
featuresets = [(gender_features(n), g) for (n,g) in names]
# Next, I use the feature extractor to process the names data, and divide the resulting
# list of feature sets into a training set and a test set. The training set is used to train a
# new “naive Bayes” classifier.
dev_test_set = featuresets[500:1000]
train_set = featuresets[1000:]
test_set = featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print "dev_test_accuracy"
print nltk.classify.accuracy(classifier, dev_test_set)
print "test_accuracy"
print nltk.classify.accuracy(classifier, test_set)
print "train_set"
print nltk.classify.accuracy(classifier, train_set)
# I can examine the classifier to determine which features it found most effective
# for distinguishing the last letters and which suffixes in some words (70 words)
classifier.show_most_informative_features(70)
