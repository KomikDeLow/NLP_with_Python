# fine
#
#Presented by Tetiana Kobryn

# Chapter 6, Ex. 2
#Using any of the three classifiers described in this chapter, and any features 
#you can think of, build the best name gender classifier you can. Begin by 
#splitting the Names Corpus into three subsets: 500 words for the test set, 500 
#words for the dev-test set, and the remaining 6,900 words for the training set. 
#Then, starting with the example name gender classifier, make incremental 
#improvements. Use the devtest set to check your progress. Once you are 
#satisfied with your classifier, check its final performance on the test set. 
#How does the performance on the test set compare to the performance on the 
#dev-test set? Is this what you had expect?


import nltk
from nltk.corpus import names
# preparing a list of examples and corresponding class labels
names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])
# building feature extractor function
def gender_features(name):
        features = {}
        features["lastletter"] = name[-1].lower()
        features["suffix1"] = name[-2:].lower()
        features["suffix2"] = name[-3:].lower()
        features["suffix3"] = name[-4:].lower()
        return features
#dividing the resulting list of feature sets into a train, devtest and test sets   
featuresets = [(gender_features(n), g) for (n,g) in names]
train_set = featuresets[1000:]
dev_test_set = featuresets[500:1000]
test_set = featuresets[:500]
# building a classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)
# evaluating accuracy
print "dev_test_accuracy"
print nltk.classify.accuracy(classifier, dev_test_set)
print "test_accuracy"
print nltk.classify.accuracy(classifier, test_set)
# showing most informative features of the classifier
classifier.show_most_informative_features(20)
