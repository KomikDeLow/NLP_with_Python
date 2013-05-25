import nltk
# import Movie Reviews Corpus, which categorizes each review as positive or negative
from nltk.corpus import movie_reviews
import random
documents=[(list(movie_reviews.words(fileid)),category)
	   for category in movie_reviews.categories()
	   for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
# define a feature extractor for documents, so the classifier will know which aspects of the data it should pay attention to
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features=all_words.keys()[:500]
# define a feature extractor that simply checks whether each of these words is present in a given document
def document_features(document):
	document_words=set(document)
	features={}
	for word in word_features:
		features['contains(%s)' %word]=(word in document_words)
		return features # return features of the function to use it again
# train and test our classifier for document classification
featuresets= [(document_features (p), m) for (p,m) in documents]
train_set, test_set=featuresets[100:], featuresets[:100]
# build a classifier
classifier=nltk.NaiveBayesClassifier.train(train_set)
# compute its accuracy on the test set to check how reliable the resulting classifier is
print nltk.classify.accuracy(classifier, test_set)
0.49
# use show_most_informative_features() to find out which features the classifier found to be most informative
classifier.show_most_informative_features(30)



