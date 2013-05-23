#analyzer of accuracy
#should rise
#words with frequency=<2
#change to UNK
#create analyzers

import nltk
from nltk.corpus import brown
brown_tagged_sents=brown.tagged_sents(categories='news')
vocab = nltk.FreqDist(brown.words(categories='news'))
mapping = nltk.defaultdict(lambda: 'UNK')
for v,t in brown.tagged_words(categories='news'):
    if vocab[v]>2:
        mapping[v],t = v,t

new_tagged_sents=[]
for i in brown.tagged_sents(categories='news'):
    new_tagged_sents.append([(mapping[v],t) for (v,t) in i])

brown.tagged_sents(categories='news')[10]
new_tagged_sents[10]
size = int(len(brown_tagged_sents) * 0.9)
train_sents1 = brown_tagged_sents[:size]
test_sents1 = brown_tagged_sents[size:]
train_sents2 = new_tagged_sents[:size]
test_sents2 = new_tagged_sents[size:]
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents1, backoff=t0)
t2 = nltk.BigramTagger(train_sents1, backoff=t1)
print t2.evaluate(test_sents1)
t1 = nltk.UnigramTagger(train_sents2, backoff=t0)
t2 = nltk.BigramTagger(train_sents2, backoff=t1)
print t2.evaluate(test_sents2)
t2 = nltk.BigramTagger(train_sents2, backoff=t0)
print t2.evaluate(test_sents2)


