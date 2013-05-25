# Roman Borys PRLs-11
import nltk, random
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category) # Creating the list of movie reviews
	     for category in movie_reviews.categories()
	     for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]
# Creating function for a search
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
	        features['contains(%s)' % word] = (word in document_words)
    return features
# Dividing data
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
#Creating classifiers
print nltk.classify.accuracy(classifier, test_set)
print classifier.show_most_informative_features(30)
