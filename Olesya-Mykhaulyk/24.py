# TODO
# unexpected indent!!!
# What does your program do?

#Olesya Mykhaulyk ALs-12
import nltk
from nltk.corpus import brown
brown_sents=brown.sents()
brown_tagged_sents=brown.tagged_sents() #dostypaemos do re4en
size=int(len(brown_tagged_sents)*0,9)
train_sents=brown_tagged_sents[:size] # dani na jakuh provodutsa trenyvanja
    for n in range(6):  #zbilwyemo n do 6 i robumo otsinky robotu ngramma
        ngram=nltk.NgramTagger(n,train=brown_tagged_sents)
        print n, ngram.evaluate(brown_tagged_sents[size:]) # otsinka robotu i vuvedenja rezyltativ

