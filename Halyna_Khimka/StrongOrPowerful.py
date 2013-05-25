# TODO
# The accuracy is low
#


#Word Choice: Strong or Powerful
#Halyna Khimka
#Chapter 6.6
#
#
"""
The Program StrongOrPowerful defines with what kind of synonymous words patterns the noun
on the base of context. The featureset is extracted from corpus BROWN.
The function Prediction enables to define the correct adjective for a given noun.

With trigrams the accuracy is really higher=)

"""
import nltk
from nltk.corpus import brown
featureset=[]
context={}

for tagged_sent in brown.tagged_sents():
	for (w1,t1), (w2,t2) in nltk.bigrams(tagged_sent):
		if t1.startswith('JJ') and w1 == 'strong': 
			context[w2]=t2
			featureset.append((context,w1))
			context={}
		if t1.startswith('JJ') and w1 == 'powerful':
			context[w2]=t2
			featureset.append((context,w1))
			context={}

for tagged_sent in brown.tagged_sents():
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(tagged_sent):
		if t1.startswith('JJ') and w1 == 'strong': 
			context[w2]=t2
			context[w3]=t3
			featureset.append((context,w1))
			context={}
		if t1.startswith('JJ') and w1 == 'powerful':
			context[w2]=t2
			context[w3]=t3
			featureset.append((context,w1))
			context={}			


			
size = int(len(featureset)* 0.1)
train_set, test_set = featureset[size:], featureset[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)

def Prediction(word, tag):
        print 'Word', word, 'patterns with', classifier.classify({word:tag})

			
