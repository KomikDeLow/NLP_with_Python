# TODO
# Your program doesn't  work correctly
#

#
# zad. 2 rozdil 6
# Daria Morozova
# var.11


import nltk
from nltk.corpus import names
import random
def gender_features(name):       # morphological characteristics of feature set
        features={}
	features['firstletter']=name[0].lower() #first letter of the name
	features['lastletter']=name[-1:].lower() # last letter of the name
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		features["count(%s)" % letter] = name.lower().count(letter)
		features["has(%s)" % letter] = (letter in name.lower())
		return features #???
names = ([(name, 'male') for name in names.words('male.txt')] +
       [(name, 'female') for name in names.words('female.txt')]) #building a set of data

random.shuffle(names) # shuffling the set of names randomly
featuresets = [(gender_features(n), g) for (n,g) in names] #building data for the classifier
test_set=featuresets[:500]    #dividing data on test_set and train_set
dev_test_set=featuresets[500:1000]
train_set=featuresets[1000:]
classifier = nltk.NaiveBayesClassifier.train(train_set) 
print nltk.classify.accuracy(classifier, dev_test_set) #evaluating accuracy
print nltk.classify.accuracy(classifier, test_set)
