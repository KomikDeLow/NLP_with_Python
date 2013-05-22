# Veroonika Klantsak ALs-11

# yakuj vidsotok tupiv sliv markyetsya tumu samumu tegamu
import nltk
from nltk.corpus import brown
def persentage(text):
    data=nltk.ConditionalFreqDist((word.lower(),tag) for (word,tag)in text)
    t=0
    a=0
    for word in data.conditions():
        if len(data[word])==1:
            a+=1
            t+=1
            return a*100/t



print persentage(nltk.corpus.brown.tagged_words())
print persentage(nltk.corpus.treebank.tagged_words())
