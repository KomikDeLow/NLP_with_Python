>>> import nltk
from nltk
>>> from nltk.corpus import brown
>>> featureset=[]
>>> context={}
>>> for tagged_sent in brown.tagged_sents():
  for (w1,t1), (w2,t2) in nltk.bigrams(tagged_sent):
            if t1.startswith('JJ') and w1 == 'strong':
	context[w2]=t2
	featureset.append((context,w1))
	context={}
	if t1.startswith('JJ') and w1 == 'powerful':
	context[w2]=t2
	featureset.append((context,w1))
	context={}
>>> featureset[100]
({'to': 'TO'}, 'strong')
>>> featureset[150]
({'emotion': 'NN'}, 'strong')
>>> featureset[202]
({'and': 'CC'}, 'strong')
>>> size = int(len(featureset)* 0.1)
>>> train_set, test_set = featureset[size:], featureset[:size]
>>> classifier = nltk.NaiveBayesClassifier.train(train_set)
>>> nltk.classify.accuracy(classifier, test_set)
0.59999999999999998
>>> classifier.classify({'sales':'NNS'})
'strong'
>>> classifier.classify({'chip':'NN'})
'strong'
>>> classifier.classify({'body':'NN'})
'powerful'
>>> classifier.classify({'factor':'NN'})
'powerful'
