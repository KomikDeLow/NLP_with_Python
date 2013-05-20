# Daria Morozova
# Var 11
# Chapter 6 Ex. 2
# Corrected


import nltk
from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')] +
[(name, 'female') for name in names.words('female.txt')])
def gender_features(name):
	features = {}
	features["firstletter"] = name[1].lower()
	features['lastletter']=name[-1:].lower()
	return features



featuresets = [(gender_features(n), g) for (n,g) in names]
test_set=featuresets[500:]
dev_test_set = featuresets[500:1000]
train_set = featuresets[:6900]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
print nltk.classify.accuracy(classifier, dev_test_set)
print classifier.show_most_informative_features(40)
