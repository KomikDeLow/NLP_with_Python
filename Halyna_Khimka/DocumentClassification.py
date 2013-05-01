#Halyna Khimka
#Document Classifier
#
"""
This program automatically tags new documents with appropriate category labels using
most frequent words.

Function TypeOfDoc(word1, word2) defines in what type of documents given words are the most frequent.

Example of function usage:
>>> TypeOfDoc('next', 'marriage')

Also the function can be modified and identify the type of document using more words. 
"""
import nltk, random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn

documents = [(list(movie_reviews.words(fileid)), category)
       for category in movie_reviews.categories()
       for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]

def document_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features

featuresets = [(document_features(d), c) for (d,c) in documents]

for word in all_words.keys()[:300]:
    if all_words[word]<all_words[all_words.keys()[200]]:
           for synset in wn.synsets(word):
                  for hypernyms in synset.hypernyms():
                          for l_names in hypernyms.lemma_names:
                                   if l_names in all_words.keys()[:200]:
                                           if word not in word_features:
                                                   wors_features.append(word)

print 'Words:', len(word_features)
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)

def TypeOfDoc(word1, word2):
    print classifier.classify({'contains(%s)' % word: True,'contains(%s)' % word: True })

