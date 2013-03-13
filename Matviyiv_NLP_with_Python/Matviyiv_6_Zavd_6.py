import nltk
import random
from nltk.corpus import brown
tagged_words=brown.tagged_words()
bigram_list=nltk.bigrams(tagged_words)
bigram_needed=[w for w in bigram_list if w[0][0].lower() in ['strong','powerful']]
def feature11((w,p)):
	return {'word':p[0],'Pos':p[1]}
featureSet=[]
for word in bigram_needed:
	featureSet.append((feature11(word),word[0][0]))
test_data=featureSet[:120]
train_data=featureSet[120:]

classifier = nltk.NaiveBayesClassifier.train(train_data)

print 'Clasifier accuraci: ',100.0 * nltk.classify.accuracy(classifier, test_data),'%'
