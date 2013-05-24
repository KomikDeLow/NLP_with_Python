import nltk
 from nltk.corpus import movie_reviews
 documents = [(list(movie_reviews.words(fileid)), category)
	     for category in movie_reviews.categories()
	      for fileid in movie_reviews.fileids(category)]
# defining a feature extractor for documents
 all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# individual words are present in a given document.
 word_features = all_words.keys()[:2000]
def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
		return features

	
 featuresets = [(document_features(d), c) for (d,c) in documents]
 train_set, test_set = featuresets[100:], featuresets[:100]
 classifier = nltk.NaiveBayesClassifier.train(train_set)
 classifier.show_most_informative_features(30)
print
