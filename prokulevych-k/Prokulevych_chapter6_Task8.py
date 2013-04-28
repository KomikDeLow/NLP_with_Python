#Прокулевич К. ПРЛс-11, Розділ 6 №8
#Using the WordNet lexicon, augment the movie review
#document classifier presented in this chapter to use features
#that generalize the words that appear in a document,
#making it more likely that they will match words found in the training data
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
documents = [(list(movie_reviews.words(fileid)), category)
#construct a list of documents, labeled with the appropriate categories
	     for category in movie_reviews.categories()
	     for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]#constructing a list of the 2,000 most frequent words in the overall corpus
def document_features(document): #define a feature extractor
	document_words = set(document)#compute the set of all words in a document
	features = {}
	for word in word_features:
	    features['contains(%s)' % word] = (word in document_words)
	return features
#Training and testing a classifier for document classification:
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[1800:], featuresets[:200]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)#compute classifier accuracy on the test set
#increasing the frequency:
for word in all_words.keys():
	if all_words[word]<70:
		for synset in wn.synsets(word):
			for hypernyms in synset.hypernyms():
				for l_names in hypernyms.lemma_names:
					all_words.inc(l_names)

word_features1 = all_words.keys()[:2000]
print len([word for word in word_features1 if word not in word_features])#how changed the list of most frequency words
word_features = all_words.keys()[:2000]
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[1800:], featuresets[:200]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
#accuracy didn't increase
