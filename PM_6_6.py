# TODO
# Comments?
#


import nltk
from nltk.corpus import movie_reviews
import random
documents=[(list(movie_reviews.words(fileid)),category)
	   for category in movie_reviews.categories()
	   for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features=all_words.keys()[:100]
def document_features(document):
	document_words=set(document)
	features={}
	for word in word_features:
		features['contains(%s)' %word]=(word in document_words)
		return features # ?????
featuresets= [(document_features (p), m) for (p,m) in documents]
train_set, test_set=featuresets[100:], featuresets[:100]
classifier=nltk.NaiveBayesClassifier.train(train_set)
classifier.classify(document_features('powerful'))
'neg'
classifier.classify(document_features('strong'))
'neg'
classifier.classify(document_features('chip'))
'neg'
classifier.classify(document_features('sales'))
'neg'
print nltk.classify.accuracy(classifier, test_set)
0.49
classifier.show_most_informative_features(5)


