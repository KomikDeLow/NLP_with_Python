# Veronika Klantsak ALs-11

# imennuku yaki chastishe zystrichayutsya v odn. nizh v mnozhuni

import nltk
from nltk.corpus import brown
s=[]
a=[]
for (word, tag) in brown.tagged_words(categories='news'): # powyk sliv yaki mayut' teg imennuka v odnuni
    if tag=='NN':
        s.append(word)



fdist = nltk.FreqDist(s) #stvorennya chastotnogo spusky 
for (word, tag) in brown.tagged_words(categories='news'):
    if tag=='NNS':
        a.append(word[:-1])



fdist1 = nltk.FreqDist(a)
for i in fdist.keys(): # porivnyannya chastotu vxodzhennya v spusku imennukiv.
    if fdist1[i]>fdist[i]:
        print i
        
