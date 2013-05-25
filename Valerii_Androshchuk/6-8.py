# Valerii Androshchuk APL(s)-13
# Chapter 6, Task 8
# Using WN lexicon, augment the movie review document classiier to use features
# that genalize the words that appear in a document...

import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet
# Importing WN to use it in further work.

documents = [(list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
w_f = words.keys()[:300]
def document_features(document):
    doc_words = set(document)
    features = {}
    for word in w_f:
      features[word] = (word in doc_words)
    return features
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[300:], featuresets[:400]
classifier = nltk.NaiveBayesClassifier.train(train_set)
# Setting classifier.

print "Accuracy BEFORE adding synsets", nltk.classify.accuracy(classifier, test_set)
print "Features amount: ", len(w_f)
for word in words.keys()[:400]:
    if words[word] < words[words.keys()[200]]:
      for synset in wordnet.synsets(word):
        for hypernym in synset.hypernyms():
          for lemmas in hypernym.lemma_names:
            if (lemmas not in w_f):
              w_f.append(lemmas)
#Adding synsets.
              
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print "Accuracy AFTER adding synsets: ", nltk.classify.accuracy(classifier, test_set)
print "Features amount: ", len(w_f)

# Result: After adding synsets, accuracy rosen up, it means that
# It have made classifier more performant.
#Accuracy BEFORE adding synsets 0.73
#Features amount:  300
#Accuracy AFTER adding synsets:  0.742
#Features amount:  2099
