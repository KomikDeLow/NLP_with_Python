# TODO
# It doesn't work
# NameError: name 'featureSet' is not defined
# Comments?
import nltk
import random
from nltk.corpus import brown
bigramList=nltk.bigrams(brown.tagged_words()) # building a bigran list
bigram_We_need=[w for w in bigramList if w[0][0].lower() in ['strong','powerful']] # building a list of bigrams with needed words
def features((w,p)):
	return {'word':p[0],'Pos':p[1]} # extracting features needed for a tagger, and building a dictionary out of it
Set_of_features=[] 
for word in bigram_We_need:
	Set_of_features.append((features(word),word[0][0])) # building a list of features needed for training a tagger
test_set=Set_of_features[:120] # dividing data into train and test set
train_set=Set_of_features[120:]

classifier = nltk.NaiveBayesClassifier.train(train_set) # evaluating a tagger

print 'Clasifier accuraci: ', nltk.classify.accuracy(classifier, test_set)
