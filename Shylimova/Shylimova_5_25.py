# Shylimova K. Al-13
# Chapter 5 task 25

import nltk
fd= nltk.FreqDist(nltk.corpus.floresta.words ())
a= fd.keys()[:100]
print a
cfd= nltk.ConditionalFreqDist(nltk.corpus.floresta.tagged_words())
slovo= dict((word, cfd[word].max()) for word in a)
print slovo['em']
print slovo['contos']
print slovo['isso']
print slovo['ano']
print slovo['este']
unigram_tagger= nltk.UnigramTagger (model=slovo)
unigram_tagger.evaluate(nltk.corpus.floresta.tagged_sents())
b= nltk.corpus.floresta.tagged_sents ()
c= nltk.DefaultTagger('NN')
c1 = nltk.UnigramTagger(b, backoff=c)
c2=nltk.BigramTagger(b, cutoff=0, backoff=c1)
print c2.evaluate(b)
from nltk.corpus import treebank
d=nltk.corpus.treebank.tagged_sents()
c= nltk.DefaultTagger('NN')
c1 = nltk.UnigramTagger(d, backoff=c)
c2=nltk.BigramTagger(d, cutoff=0, backoff=c1)
print c2.evaluate(d)
