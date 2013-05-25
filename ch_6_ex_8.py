#Iuliia Tsymbalista
# CHAPTER 6 EX.8
# task:
#The dialogue act classifier assigns labels to individual posts, without considering
#the context in which the post is found. However, dialogue acts are highly dependent
#on context, and some sequences of dialogue act are much more likely than
#others. For example, a ynQuestion dialogue act is much more likely to be answered
#by a yanswer than by a greeting. Make use of this fact to build a consecutive classifier
#for labeling dialogue acts. Be sure to consider what features might be useful.
#See the code for the consecutive classifier for part-of-speech tags in Example 6-5
#to get some ideas.


#For comparison, check out the impact of hyponyms insted of  hypernyms.

import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
documents = [(list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)[:100]]
random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
print len(all_words)
word_features = all_words.keys()[:200]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
        return features
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[80:], featuresets[:20]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)

# add more frequent word to the list
for word in all_words.keys()[:300]:
    if all_words[word]< all_words[all_words.keys()[200]]:
        for synset in wn.synsets(word):
            for hyponyms in synset.hyponyms():
                for l_names in hyponyms.lemma_names:
                    if l_names in all_words.keys()[:200]:
                        if word not in word_features:
                            word_features.append(word)
                            
#the new word count in the list
print len(word_features)
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[80:], featuresets[:20]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print 'Accuracy:'
print nltk.classify.accuracy(classifier, test_set)

