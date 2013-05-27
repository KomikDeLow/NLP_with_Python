##5_28

import nltk ## importyemo nltk 
from nltk.corpus import brown ##import korpus brown
size = int(len(brown.tagged_sents(categories='news', simplify_tags=True)) * 0.9)
## zadaemo simplified tagset (by discarding all but the first character of each tag name)
train=brown.tagged_sents(categories='news', simplify_tags=True)[:size]##zadaemo train set
test=brown.tagged_sents(categories='news', simplify_tags=True)[size:]##zadaemo test set
t0 = nltk.DefaultTagger('NN')##experiment with tagger
t1 = nltk.UnigramTagger(train, backoff=t0)
t2 = nltk.BigramTagger(train, backoff=t1)
t3 = nltk.TrigramTagger(train, backoff=t2)
t4 = nltk.NgramTagger(4, train, backoff=t3)
t0 = nltk.DefaultTagger('N')
t0.evaluate(test)##Resyltatu

t1.evaluate(test)

t3.evaluate(test)

t2.evaluate(test)

t4.evaluate(test)

