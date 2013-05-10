# fine
#
# TODO
# Comments?
#
# Building a two gender classifiers on basis of name corpus in nltk. Detecting the accuraci of both classifiers.
import nltk
import random
from nltk.corpus import names

namesSet = ([(name, 'male') for name in names.words('male.txt')]+
            [(name, 'female') for name in names.words('female.txt')])# building a set of data (name + gander)
random.shuffle(namesSet) # shufling the set of names randomly
def gender_features(word):
	return {'last_letter': word[-1]} # building a function thet extracts features used in the tagger (one last letter in our case)

featuresets = [(gender_features(n), g) for (n,g) in namesSet] # buildeng data for the classifier ( feature + gender)
test_set=featuresets[:500]      #
dev_test_set=featuresets[500:1000]#
training_set=featuresets[1000:]# dividing test and train data
classifier = nltk.NaiveBayesClassifier.train(training_set) # training a classifier


print 'Accurasi of standart classifier: ',100.0*(nltk.classify.accuracy(classifier, dev_test_set)),'%' # Evaluationg a classifier


def gender_features2(word):
	return {'two_last_letters': word[-2:]} # A second function for extracting features (two last letters of names)
featuresets2 = [(gender_features2(n), g) for (n,g) in namesSet] # building second set of data for training another classifier
test_set2=featuresets2[:500]
dev_test_set2=featuresets2[500:1000]
training_set2=featuresets2[1000:]
classifier2 = nltk.NaiveBayesClassifier.train(training_set2) # training a second classifier
print 'Accurasi of classifier using two last letters: ',100.0*(nltk.classify.accuracy(classifier2, dev_test_set2)),'%' # Evaluating the second classifier
print '==========================================================='
print 'Accurasi of standart classifier (on test_set): ',100.0*(nltk.classify.accuracy(classifier, test_set)),'%'# accurasi based on test_set
print 'Accurasi of classifier using two last letters (on test_set): ',100.0*(nltk.classify.accuracy(classifier2, test_set2)),'%' # accurasi based on train_set
