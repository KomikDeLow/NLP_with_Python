# TODO
# Comments?
# It doesn't work
# NameError: name 'test_set' is not defined


import nltk
import random
from nltk.corpus import names

Set_of_names = ([(name, 'male') for name in names.words('male.txt')]+
            [(name, 'female') for name in names.words('female.txt')])
random.shuffle(Set_of_names)
def gender_features(word):
	return {'last_letter': word[-1]}

words_with_features = [(gender_features(n), g) for (n,g) in Set_of_names]
test_data=words_with_features[:500]
dev_test_data=words_with_features[500:1000]
training_data=words_with_features[1000:]
classifier = nltk.NaiveBayesClassifier.train(training_data)

print 'Accurasy of standart classifier: ',100.0*(nltk.classify.accuracy(classifier, dev_test_data)),'%'

def gender_features2(word):
	return {'two_last_letters': word[-2:]}
featuresets2 = [(gender_features2(n), g) for (n,g) in Set_of_names]
test_data2=featuresets2[:500]
dev_test_data2=featuresets2[500:1000]
training_data2=featuresets2[1000:]
classifier2 = nltk.NaiveBayesClassifier.train(training_data2)
print 'Accurasy of classifier using two last letters: ', nltk.classify.accuracy(classifier2, dev_test_data2)
print 'Accurasy of standart classifier (on test_set): ', nltk.classify.accuracy(classifier, test_set)
print 'Accurasy of classifier using two last letters (on test_set): ', nltk.classify.accuracy(classifier2, test_set2)
