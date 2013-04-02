# fine
#
# Name_Classifier
# Author: Halyna Khimka
# Chapter 6, Task 2 Natural Language Processing with Python
#
"""
Name_Classifier
There is my Name Classifier in this module.My Classifier decides whether the name is male or female on 
the base of some features set. This features set includes such morphological characteristics like
first letter, last letter, two last letters and three last letters of the given name.
Such feature as length of the name is not informative and makes the classifier performance worse. (features['name_length']=len(name.lower()))

This module evaluates the performance of the classifier on the development set and test set.
Also this module generates the list of errors that the classifier makes when predicting name genders.
To see the list of errors we can add such command ti this module:
for (tag, guess, name) in sorted(errors): # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)
Also there is function of the module gender_predicting(name) which defines whether the name is male or female. 
"""
import nltk
def gender_features(name):
        features={}
        features['firstletter']=name[0].lower()
        features['one_lastletter']=name[-1:].lower()
        features['two_lastletters']=name[-2:].lower()
        features['three_lastletters']=name[-3:].lower()
        if len(name)>3: 
            features['four_lastletters']=name[-4:].lower()
        return features

    
from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')] +
       [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)
dev_names, train_names, test_names = names[:500], names[1000:], names[500:1000]
train_set = [(gender_features(n), g) for (n,g) in train_names]
devset = [(gender_features(n), g) for (n,g) in dev_names]
test_set = [(gender_features(n), g) for (n,g) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
errors = []
for (name, tag) in dev_names:
        guess = classifier.classify(gender_features(name))
        if guess != tag:
            errors.append( (tag, guess, name) )

def gender_predicting(name):
        classifier.classify(gender_features(name))
        print 'Name:', name, 'Gender:',classifier.classify(gender_features(name))
    
print 'Evaluation of Names Classifier Performance on DevTest Data:', nltk.classify.accuracy(classifier, devset), '\n', 'Evaluation of Names Classifier Performance on Test Data:', nltk.classify.accuracy(classifier, test_set), '\n', classifier.show_most_informative_features(20)
