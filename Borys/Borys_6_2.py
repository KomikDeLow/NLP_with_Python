import nltk
from nltk.corpus import names
names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])# Variable that contains information

#Creating function
def gender_features(name):
        features = {}
        features["lastletter"] = name[-1].lower()
        features["suffix1"] = name[-2:].lower()
        features["suffix2"] = name[-3:].lower()
        features["suffix3"] = name[-4:].lower()
        return features
#Sorting corpus into three parts
featuresets = [(gender_features(n), g) for (n,g) in names]
train_set = featuresets[500:]
dev_test_set = featuresets[500:1000]
test_set = featuresets[1000:]
#Creating NaiveBayes classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, dev_test_set)
print nltk.classify.accuracy(classifier, test_set)
print classifier.show_most_informative_features(20)

