# Maryna Ivaniv PRLs-11 Chapter5 Ex.27
#Inspect the confusion matrix for the bigram tagger t2 defined in Section 5.5, and
#identify one or more sets of tags to collapse. Define a dictionary to do the mapping,
#and evaluate the tagger on the simplified data.

import nltk
from nltk.corpus import brown
brown.categories
brown.categories()
brown_tagged_sents = brown.tagged_sents(categories='government')
brown_sents = brown.sents(categories='government')
size = int(len(brown_tagged_sents) * 0.9)
size
train_sents = brown_tagged_sents[:1000]
test_sents = brown_tagged_sents[1500:]
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t2.evaluate(test_sents)
0.76199405241492468
test_tags = [tag for sent in brown.sents(categories='government')
       for (word, tag) in t2.tag(sent)]
gold_tags = [tag for (word, tag) in brown.tagged_words(categories='government')]
print nltk.ConfusionMatrix(gold_tags, test_tags)
cfd= nltk.ConfusionMatrix(gold_tags, test_tags)
collapses=nltk.defaultdict(int)

for i in range(int(len(test_tags))):
	if test_tags[i] !=gold_tags [i]:
		pair=(test_tags [i], gold_tags [i])
		if pair not in collapses:
			collapses[pair]+=1
			
print cfd.key(), '\n''List of collapses', '\n', 'Evaluation of the tagger t2:', t2.evaluate(test_sents)
