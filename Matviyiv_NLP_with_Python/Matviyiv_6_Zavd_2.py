import nltk
import random
from nltk.corpus import names

namesSet = ([(name, 'male') for name in names.words('male.txt')]+
            [(name, 'female') for name in names.words('female.txt')])
random.shuffle(namesSet)
def gender_features(word):
	return {'last_letter': word[-1]}

featuresets = [(gender_features(n), g) for (n,g) in namesSet]
test_set=featuresets[:500]
dev_test_set=featuresets[500:1000]
training_set=featuresets[1000:]
classifier = nltk.NaiveBayesClassifier.train(training_set)


print 'Accurasi of standart classifier: ',100.0*(nltk.classify.accuracy(classifier, dev_test_set)),'%'


def gender_features2(word):
	return {'two_last_letters': word[-2:]}
featuresets2 = [(gender_features2(n), g) for (n,g) in namesSet]
test_set2=featuresets2[:500]
dev_test_set2=featuresets2[500:1000]
training_set2=featuresets2[1000:]
classifier2 = nltk.NaiveBayesClassifier.train(training_set2)
print 'Accurasi of classifier using two last letters: ',100.0*(nltk.classify.accuracy(classifier2, dev_test_set2)),'%'
print '==========================================================='
print 'Accurasi of standart classifier (on test_set): ',100.0*(nltk.classify.accuracy(classifier, test_set)),'%'
print 'Accurasi of classifier using two last letters (on test_set): ',100.0*(nltk.classify.accuracy(classifier2, test_set2)),'%'
