import nltk, random
from nltk.corpus import brown
suffix_fdist = nltk.FreqDist()
for word in brown.words():
	word = word.lower()
	suffix_fdist.inc(word[-1:])
	suffix_fdist.inc(word[-2:])
	suffix_fdist.inc(word[-3:])
common_suffixes = suffix_fdist.keys()[:10]
common_suffixes = suffix_fdist.keys()[:10]
def pos_features(word): # choosing right feature
	features = {}
	for suffix in common_suffixes:
		features['endswith(%s)' % suffix] = word.lower().endswith(suffix)
	return features

tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n), g) for (n,g) in tagged_words]
size = int(len(featuresets) * 0.1) #building data sets for training test
train_set, test_set = featuresets[size:], featuresets[:size] # building and train classifiers
classifier = nltk.DecisionTreeClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)# evaluating the accurase of classifiers

classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)

classifier = nltk.MaxentClassifier.train (train_set)
print nltk.classify.accuracy(classifier, test_set)

