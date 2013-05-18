# Maryna Ivaniv PRLs-11 Chapter 6 Ex.4
#Using the movie review document classifier discussed in this chapter, generate
#a list of the 30 features that the classifier finds to be most informative. Can you
#explain why these particular features are informative? Do you find any of them
#surprising?

import nltk
from nltk.corpus import movie_reviews
import random
documents = [(list(movie_reviews.words(fileid)), category)# categorises each review as positive or negative
 for category in movie_reviews.categories()
 for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)# define a feature extractor for documens
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features=all_words.keys() [:2500] # most frequent words of the overal corpus
def document_features(document): # chech if the word present in a given document
	 document_words= set(document)# compute the set of all words in a document
	 features= {}
	 for word in word_features:
		  features['contains(%s)' % word] = (word in document_words)
		  return features

print document_features(movie_reviews.words('pos/cv957_8737.txt'))
{'contains(waste)': False, 'contains(lot)': False,}
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[:100], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)# To check how resulting classifier is, we compute its accuracy on the test set
classifier.show_most_informative_features(5)# found the most informative features
