#Oksana Pokladok

import nltk
from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')] +
[(name, 'female') for name in names.words('female.txt')])  # bydyjy nabir danuh
def gender_features(name):   # morfologi4ni harakterustuku feature set
	features = {}
	features["firstletter"] = name[1].lower() # persha bykva imeni
	features['lastletter']=name[-1:].lower()  # ostannja bykva imeni
	return features



featuresets = [(gender_features(n), g) for (n,g) in names] # stvorennja danuj dlja klasufikatora
test_set=featuresets[500:]                                 # podil danuh na test_set ta train_set
dev_test_set = featuresets[700:1200]
train_set = featuresets[:7100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)         # ocinka to4nosti
print nltk.classify.accuracy(classifier, dev_test_set)
print classifier.show_most_informative_features(40)