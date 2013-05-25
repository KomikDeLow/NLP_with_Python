
import nltk
from nltk.corpus import brown
featureset = []
S = "strong"
P = "powerful"
for tagged_sent in brown.tagged_sents():
    for b1, b2 in nltk.bigrams(tagged_sent):
        if b1[1].startswith('JJ') and b1[0] == S:
            featureset.append(({b2[0]: b2[1]}, S))
        elif b1[1].startswith('JJ') and b1[0] == P:
            featureset.append(({b2[0]: b2[1]}, P))
print len(featureset)
size = int(len(featureset) * 0.1)
train_set, test_set = featureset[size:], featureset[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
nltk.classify.accuracy(classifier, test_set)
for feature in test_set:
    print classifier.classify(feature[0]), feature[0].keys()[0], feature
