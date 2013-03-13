import nltk
import types
from nltk.corpus import senseval
instances = senseval.instances('serve.pos')
features=[]
for inst in instances:
	x=[]

for i in inst.context:
	if type(i) == types.TupleType:
		x.append(i)
	elif type(i) == types.StringType:
		 x.append(("None",i))
	y={"word": inst.word,"position": inst.position,}
	z=dict(x)
	y.update(z)
	features.append((y,' '.join(inst.senses)))

	
size = int(len(features) * 0.1)
train_set, test_set = features[size:], features[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
	
