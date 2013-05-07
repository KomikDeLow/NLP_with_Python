# TODO
# Please, read Ch4, because your programming style is bad
# entropy???


#Iryna Shtanhret, Al-13,Task 5 Chapter6. 
#the task was to select one of the classification
#i have choosen gender detection, and built classifiers for the task NaiveBayesClassifier, Decision Trees
import nltk #import data
from nltk.corpus import names#from the corpus importing names
import random#This module contains a number of random number generators.
#The random module provides tools for making random selections:
import math#importing mathematic functions
names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)#shuffle names
def gender_features(word): ##function for determining the gender of name
#The first step in creating a classifier is deciding what features of the input are relevant, and how to encode those features. 
#For this example, we'll start by just looking at the final letter of a given name. 
#The following feature extractor function builds a dictionary containing relevant information about a given name
    return {'last_letter': word[-1]}
featuresets = [(gender_features(n), g) for (n,g) in names]
size = int(len(featuresets) * 0.1)#setting a size for a testing data
train_set, test_set = featuresets[size:], featuresets[:size]

#NaiveBayesClassifier
#A NaiveBayesClassifier provides a trainable naive Bayes text classifier, with tokens as features. 
#A classifier is constructed from a set of categories and a tokenizer factory.
# The token estimator is a unigram token language model with a uniform whitespace model and an optional n-gram character language model for smoothing unknown tokens.
naiveBayesClassifier = nltk.NaiveBayesClassifier.train(train_set)
productivity=nltk.classify.accuracy(naiveBayesClassifier, test_set)#with this procedure we are getting basis accuracy
#result from productivity from BayesClassifier
def entropy(labels):## function for determining the gender of names using entropy
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
    return -sum([p * math.log(p,2) for p in probs])
productivity=entropy(['male', 'female', 'male', 'male'])## result of productivity from entropy
##the function entropy show better results that's why i used it here.
