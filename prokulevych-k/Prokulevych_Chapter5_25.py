# TODO
# plagiarism!!!
#

import nltk
fd= nltk.FreqDist(nltk.corpus.floresta.words ())
a= fd.keys()[:150]
a
print a
cfd= nltk.ConditionalFreqDist(nltk.corpus.floresta.tagged_words())
b= dict((word, cfd[word].max()) for word in a)
b['primeiro']
print b['primeiro']
b['sempre']
print b['sempre']
b['novo']
print b['novo']
b['Se']
print b['Se']
unigram_tagger= nltk.UnigramTagger (model=b)
unigram_tagger.evaluate(nltk.corpus.floresta.tagged_sents())
print unigram_tagger.evaluate(nltk.corpus.floresta.tagged_sents())
c= nltk.corpus.floresta.tagged_sents ()
t= nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(c, backoff=t)
t2=nltk.BigramTagger(c, cutoff=0, backoff=t1)
t2.evaluate(c)
print t2.evaluate(c)
from nltk.corpus import treebank
d=nltk.corpus.treebank.tagged_sents()
t= nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(d, backoff=t)
t2=nltk.BigramTagger(d, cutoff=0, backoff=t1)
t2.evaluate(d)
print t2.evaluate(d)
