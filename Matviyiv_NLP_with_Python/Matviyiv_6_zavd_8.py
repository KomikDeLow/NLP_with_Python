# building a document classifier on the basis of the movie_rewiev classifier
# and using the Word net added lexicon for greater accuracy of tagging the reviews

import nltk
import random
from nltk.corpus import wordnet as wn
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords

def wn_use_test(word):
    word1=[]
    word1=wn.synsets(word)
    test3=[]
    if len(word1)==0:
        test3.append(word)
        return test3
    else:
        test3.append(word)
        test=[]
        test=word1[0].hypernyms()
        if len(test)==0:
            return test3
        else:
            test2=[]
            test2=test[0].lemma_names
            wordstr=''
            for item in test2:
                for let in item:
                    if let=='_':
                        wordstr=wordstr+' '
                    else:
                        wordstr=wordstr+let
                test3.append(wordstr)
                wordstr=''
            test2=[]
            return test3




documents = [(list(movie_reviews.words(fileid)), category) # creating a list of negative and positive reviews words + their class (positive or negative)
	     for category in movie_reviews.categories()
	     for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words()) # building a list of frequently used words in the rewievs
clean_list=[',','-','.',':',';','/','\'','\"','[',']','{','}','(',')','<','>','\\','!','?','*','&']
ets=stopwords.words('english')
clean_list=clean_list+ets

words_clean= [w for w in all_words.keys() if w not in clean_list] # deleting punctuation elements

word_features = words_clean[:2000] # taking out 2000 most frequent words for using in tagging

word_features2=[]
for word in word_features:
	smth3=[]
	smth3=wn_use_test(word)
	for item in smth3:
		word_features2.append(item)

print 'words used = ', len(word_features2)
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features2:
        for word2 in word:
            features['contains(%s)' % word2] = (word2 in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print 'Accuracy of classifier =', nltk.classify.accuracy(classifier, test_set)

# Added the extended words lexems to the list of words wich are cheked (and which were the most frequent)
# Unfortynetly the accuracy wasn't bigger than in your example at the blog. Please, if you have time, maybe, you could suggest some kind of changes or additions?
# Or maybe my code is wrong ?
