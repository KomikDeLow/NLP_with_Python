# TODO
# bad
# it isn't the Python modul

>>> import nltk
>>>  from nltk.corpus import movie_reviews
>>> documents = [(list(movie_reviews.words(fileid)), category)
       for category in movie_reviews.fileid.categories()
	     for fileid in movie_reviews.fileids(category)]
>>> random.shuffle(documents)
>>> all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
>>> word_features = all_words.keys() [:2000]
>>> def document_features(document):
	document_words = set(document)
	features ={}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features
>>> featuresets = [(document_features(d),c) for (d,c) in documents]
>>> classifier = nltk.NaiveBayesClassifier.train(train_set)
>>> Classifier.show_most_informative_features(30)