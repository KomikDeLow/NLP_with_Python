#Iryna Brykailo, ALs-13

import nltk
from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')]+
         [(name, 'female') for name in names.words('female.txt')]) #creating necessary data
random.shuffle(names) #shuffling the names 
def gend_feat(name):
    features = {}
    features['firstletter']=name[0].lower()
    features['lastletter']=name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    return features #building the function that extracts features (count and presence of the letter)
gend_feat('Betty')
train_names=names[1000:]
devtest_names=names[500:1000]
test_names=names[:500] #dividing train and test data
train_set = [(gend_feat(n),g) for (n,g) in train_names]
devtest_set = [(gend_feat(n),g) for (n,g) in devtest_names]
test_set = [(gend_feat(n),g) for (n,g) in test_names] #building data for the classifier
classifier = nltk.NaiveBayesClassifier.train(train_set) #training the classifier
print nltk.classify.accuracy(classifier, devtest_set) #evaluating the classifier
