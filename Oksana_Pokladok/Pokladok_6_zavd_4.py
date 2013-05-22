#Oksana Pokladok
import nltk
from nltk.corpus import movie_reviews
documents=[(list(movie_reviews.words(fileid)),category)#Make a randomized list of pairs, words and category, for each fileid
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]
import random
random.shuffle(documents)
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features=all_words.keys()[:1000] # our 1000 words 
def document_features(document): #Function to create a document feature list.
    document_words=set(document)# our 1000 words, we have a feature which is the word and "true" or "false
    features={}
    for word in word_features:
        features['contains(%s)' %word]=(word in document_words)
        return features


featuresets=[(document_features(d),c) for (d,c) in documents]#here we actually call the function.
train_set, test_set=featuresets[100:],featuresets[:100]
classifier=nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier,test_set)
print classifier.show_most_informative_features(30)
