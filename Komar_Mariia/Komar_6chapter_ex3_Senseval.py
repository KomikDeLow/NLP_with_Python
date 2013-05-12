# TODO
# I don't understand what does loop do in your program
#

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

import nltk
import types
from nltk.corpus import senseval #import senseval corpus
instances = senseval.instances('serve.pos') # choose data for word 'serve'
features=[]
for inst in instances:
	comtext=[]
	for i in inst.context: #оступаємося до прикладів з корпусу senseval
		if type(i) == types.TupleType: # Якщо тип змінної "і" є Tuple
			comtext.append(i)# тоді додаємо цей елемент до списку"comtext"
		elif type(i) == types.StringType:# Якщо тип змінної "і" є String
			comtext.append(("None",i))# тоді додаємо слово "None" і цей елемент до списку"comtext"
			word_position={"word": inst.word,"position": inst.position,}#створюємо словник слів та їх позиції
			dictionary=dict(comtext)#створюємо словник та записуємо туди усе з "comtext"
			word_position.update(dictionary)#додаємо усе з словника "dictionary" до словника "word_position"
			features.append((word_position,' '.join(inst.senses)))#додаємо усе з"word_position" до "features"


	
size = int(len(features) * 0.1) # choose data size for testing
train_set, test_set = features[size:], features[:size] # divide data for train and test
classifier = nltk.NaiveBayesClassifier.train(train_set) # train classifier
print nltk.classify.accuracy(classifier, test_set) #assess the accuracy of his work
	
