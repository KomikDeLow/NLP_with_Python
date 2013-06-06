#Chapter_5_Ex_28_Fursachyk Vladyslava
import nltk #importuju nltk 
from nltk.corpus import brown #importuju korpus brown
size = int(len(brown.tagged_sents(categories='news', simplify_tags=True)) * 0.9)
#zadaju simplified tagset 
train=brown.tagged_sents(categories='news', simplify_tags=True)[:size]#zadaju train set
test=brown.tagged_sents(categories='news', simplify_tags=True)[size:]##zadaju test set
t0 = nltk.DefaultTagger('NN')#experyment z tagger
t1 = nltk.UnigramTagger(train, backoff=t0)
t2 = nltk.BigramTagger(train, backoff=t1)
t3 = nltk.TrigramTagger(train, backoff=t2)
t4 = nltk.NgramTagger(4, train, backoff=t3)
t0 = nltk.DefaultTagger('N')
t0.evaluate(test)#resul'tat

t1.evaluate(test)

t3.evaluate(test)

t2.evaluate(test)

t4.evaluate(test)

