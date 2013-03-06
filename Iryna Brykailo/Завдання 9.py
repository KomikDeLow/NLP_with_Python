import nltk
from nltk.corpus import brown
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if w2=='go':
            print t1, t3

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)

def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if w2=='went':
            print t1, t3

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)
