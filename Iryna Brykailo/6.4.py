#Iryna Brykailo, ALs-13

import nltk
from nltk.corpus import movie_reviews
import random
documents= [(list(movie_reviews.words(fileid)),category) #Creating the randomized list
        for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
words=nltk.FreqDist(w.lower() for w in movie_reviews.words()) #Frequency Distribution
word_features=all_words.keys() [:1000]
def document_features(document) # Function for creating list of features
    document_words= set(document)
    features= {}
    for word in word_features:
         features['contains(%s)' % word] = (word in document_words)
    
    return features

featuresets= [(document_features(d), c) for (d,c) in documents] #Call the function
train_set, test_set = featuresets[:100], featuresets[:100]
classifier= nltk.NaiveBayesClassifier.train(train_set)
classifier.show_most_informative_features(30)

# The classifier determined the most effective features.
#These words are informative because they have different meaning and different features
#(positive or negative)
