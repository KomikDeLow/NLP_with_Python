# Veronika Klantsak ALs-11

# imennuku yaki chastishe zystrichayutsya v odn. nizh v mnozhuni

import nltk
from nltk.corpus import brown
s=[]
a=[]
for (word, tag) in brown.tagged_words(categories='news'):
    if tag=='NN':
        s.append(word)



fdist = nltk.FreqDist(s)
for (word, tag) in brown.tagged_words(categories='news'):
    if tag=='NNS':
        a.append(word[:-1])



fdist1 = nltk.FreqDist(a)
for i in fdist.keys():
    if fdist1[i]>fdist[i]:
        print i
        
