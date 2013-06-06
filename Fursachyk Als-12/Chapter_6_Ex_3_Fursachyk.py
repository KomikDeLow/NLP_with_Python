#Chapter_6_Ex_3_Fursachyk
import nltk #importuju dani
import types
from nltk.corpus import senseval #importuju korpus Senseval v jakomu kozhen element vidpovidaje odnomu dvoznachnomu slovu. 
instances = senseval.instances('serve.pos')#zminjuju instances do potribnogo vygljadu
features=[]#porozhnij spysok
for instance in instances:
	emptylist=[]
	for i in instance.context:#odyn z metodiv dostupu do elementiv Senseval instance
		if type(i) == types.TupleType:
			emptylist.append(i)#dodavannya do porozhnjogo spysku
		elif type(i) == types.StringType:
			emptylist.append(("None",i))
	a={"word": instance.word,"position": instance.position,}
	b=dict(emptylist)
	a.update(b)
	features.append((a,' '.join(instance.senses)))
size = int(len(features) * 0.1)#vstanovlennya rozmiriv dlya testovanyh danyh
train_set, test_set = features[size:], features[:size]
classifier1 = nltk.NaiveBayesClassifier.train(train_set)#NaiveBayesClassifier vykorystovuyetsya dlya logichnogo vydilennya oznak slova
print nltk.classify.accuracy(classifier1, test_set)#resultatu
