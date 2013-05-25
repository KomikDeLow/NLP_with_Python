#Iryna Ros, PRLs-11, chapter 6, exercise 6
#The synonyms strong and powerful pattern differently (try combining them with
#chip and sales). What features are relevant in this distinction? Build a classifier that
#predicts when each word should be used.
#
import nltk
from nltk.corpus import brown
featureset=[]
context={}
for tagged_sent in brown.tagged_sents():
  for (w1,t1), (w2,t2) in nltk.bigrams(tagged_sent):
    if t1.startswith('JJ') and w1 == 'strong':
      context[w2]= t2
      featureset.append((context,w1))
      context={}
    elif t1.startswith('JJ') and w1 == 'powerful':
      context[w2]= t2
      featureset.append((context,w1))
      context={}
featureset[100]
featureset[150]
featureset[202]
size = int(len(featureset) * 0.1)
train_set, test_set = featureset[size:], featureset[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
nltk.classify.accuracy(classifier, test_set)

classifier.classify({'sales':'NNS'})
classifier.classify({'chip':'NN'})
classifier.classify({'body':'NN'})
classifier.classify({'factor':'NN'})
