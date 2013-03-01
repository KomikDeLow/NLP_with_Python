#Maschakevich Khrystyna, ALs-13
import nltk
from nltk.corpus import brown
bts=brown.tagged_sents(categories='religion')
size = int(len(bts) * 0.9)
train_sents = bts[:size] #split the data, training on 90% and testing on the remaining 10%
test_sents = bts[size:]
bigram_tagger = nltk.BigramTagger(train_sents)
brown_sents=brown.sents() # Create variable, which was appropriated sentences from corpus Brown
unseen_sent = brown_sents[4207]
bigram_tagger.tag(unseen_sent)
bigram_tagger.evaluate(test_sents)
 
