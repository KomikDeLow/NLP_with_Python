# Chapter_5_Ex_29_Mokhonova
import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents) # stvorjuju zrazok z parametrom
size = int(len(brown_tagged_sents) * 0.9)   # vyznachaju dovzhynu             
train_sents = brown_tagged_sents[:size]                    
test_sents = brown_tagged_sents[size:]
bigram_tagger = nltk.BigramTagger(train_sents)# analizuju rechennya
unseen_sent = brown_sents[3333]                 
result=bigram_tagger.evaluate(test_sents)   # rezul'tat

