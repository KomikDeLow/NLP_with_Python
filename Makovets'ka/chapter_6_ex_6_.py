#The synonyms strong and powerful pattern differently
#try combining them with chip and sales).
#What features are relevant in this distinction?
#Build a classifier that predicts when
#each word should be used

import nltk
import random
from nltk.corpus import brown
bigramList=nltk.bigrams(brown.tagged_words())
bigram_We_need=[w for w in bigramList if w[0][0].lower() in ['strong','powerful']]
def features((w,p)):
    return {'word':p[0],'Pos':p[1]}
Set_of_features=[]
for word in bigram_We_need:
    Set_of_features.append((features(word),word[0][0]))
test_set=Set_of_features[:120]
train_set=Set_of_features[120:]

classifier = nltk.NaiveBayesClassifier.train(train_set)

print 'Clasifier accuraci: ', nltk.classify.accuracy(classifier, test_set)
    
