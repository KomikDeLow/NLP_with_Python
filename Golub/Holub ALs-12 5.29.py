# Prizvuszcze / Grypa

import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents) # create an exemplar with parametr
size = int(len(brown_tagged_sents) * 0.9)     # define the lenght             
train_sents = brown_tagged_sents[:size]                    
test_sents = brown_tagged_sents[size:]
bigram_tagger = nltk.BigramTagger(train_sents)# start the method to analyze the sentance
unseen_sent = brown_sents[3333]                 
result=bigram_tagger.evaluate(test_sents)     # evaluate, conclusion: using bigram tagger is not very good idea because if a word has no tagger the next word will be withou tagger too  

