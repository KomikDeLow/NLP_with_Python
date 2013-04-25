import nltk
from nltk.corpus import brown
featureset = []
context={}
for tagged_sent in brown.tagged_sents():
	for (w1,t1),(w2,t2) in nltk.bigrams(tagged_sent):# vuburaemo vsi bigrams jaki vidnosjatsja do nawox sliv
		if t1.startswith('JJ') and w1 =='strong':# markuemo vsi bigrams v jakux perwe slovo strong jak prukmetnuk
			context[w2]=t2
			featureset.append((context,w1))
			context={}
		elif t1.startswith ('JJ') and w1 =='powerful':# markuemo vsi bigrams v jakux perwe slovo powerful jak prukmetnuk
			 context [w2] =t2
			 featureset.append((context,w1))
			 context={}

			 
featureset[100]# vzhuvannja slova
featureset[150]
featureset[250]
len(featureset) # dovzhuna dorivnye 506 prukmetnukiv, wob zbiljwutu budyemo klasuficator
size = int (len(featureset)*0.1)# buduemo klasufikator
train_set, test_set = featureset[size:], featureset[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
nltk.classify.accuracy(classifier,test_set)# chastota dorivnye 0.8
classifier.classify({'sales': 'NNS'})
classifier.classify({'chip':'NN'})
# za dopomogoy programu mu mozhemo vuznachutu chastoty vzhuvannja sliv.
# a takozh diznatusja vzhuvannja zux dvox prukmetnukiv pru cjomy nam potribno zvernytu
# yvagy na morfologichni xarakterustuku.
