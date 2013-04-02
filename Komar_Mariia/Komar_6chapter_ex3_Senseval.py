# TODO
# What do your variables x,y,z, mean?
# What do you stote in this string, dictionary, list?

# Komar Mariia Als-11
# Chapter_6, ex_3

#The Senseval 2 Corpus contains data intended to train word-sense disambiguation
#classifiers. It contains data for four words: hard, interest, line, and serve.
#Choose one of these four words, and load the corresponding data:
#       >>> from nltk.corpus import senseval
#       >>> instances = senseval.instances('hard.pos')
#       >>> size = int(len(instances) * 0.1)
#       >>> train_set, test_set = instances[size:], instances[:size]
#Using this dataset, build a classifier that predicts the correct sense tag for a given
#instance. See the corpus HOWTO at http://www.nltk.org/howto for

# What do your variables x,y,z, mean?
# x = string 
# y = dictionary
# z = list of tuples

import nltk
import types
from nltk.corpus import senseval #import senseval corpus
instances = senseval.instances('serve.pos') # choose data for word 'serve'
features=[]
for inst in instances:
	x=[]

for i in inst.context:
	if type(i) == types.TupleType:
		x.append(i)
	elif type(i) == types.StringType:
		 x.append(("None",i))
	y={"word": inst.word,"position": inst.position,} #create dictionary
	z=dict(x)
	y.update(z)
	features.append((y,' '.join(inst.senses)))

	
size = int(len(features) * 0.1) # choose data size for testing
train_set, test_set = features[size:], features[:size] # divide data for train and test
classifier = nltk.NaiveBayesClassifier.train(train_set) # train classifier
print nltk.classify.accuracy(classifier, test_set) #assess the accuracy of his work
	
