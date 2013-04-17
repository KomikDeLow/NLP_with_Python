# fine
#
#Presented by Tetiana Kobryn

#Chapter 6, Ex.4
#Using the movie review document classifier discussed in this chapter, generate
#a list of the 30 features that the classifier finds to be most informative. Can you
#explain why these particular features are informative? Do you find any of them
#surprising?


import nltk
from nltk.corpus import movie_reviews
#constructing a list of documents, labeled with the appropriate categories
documents = [(list(movie_reviews.words(fileid)), category)
     for category in movie_reviews.categories()
     for fileid in movie_reviews.fileids(category)]
#constructing a list of the 2,000 most frequent words
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]
#defining feature extractor
def document_features(document):
    #computing the set of all words in a document
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
featuresets = [(document_features(d), c) for (d,c) in documents]
#splitting data to training and test set
train_set, test_set = featuresets[100:], featuresets[:100]
#building a classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)
#showing most informative features of the classifier
classifier.show_most_informative_features(30)
print
print """As we can see not just positive(outstanding) or negative(awful)
adjectives are informative, but also some proper nouns, as for example
'seagal', 'mulan', 'damon', etc."""
