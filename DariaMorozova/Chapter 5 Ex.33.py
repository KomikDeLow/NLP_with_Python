# Daria Morozova
# Variant 11
# Chapter5 Ex.33


import nltk
from nltk.corpus import brown  # import Brown Corpus
brown_tg_words=brown.tagged_words(categories='news', simplify_tags=True)  
def futuretag(word, tag):
    dictop1=dict()
    dictop2=nltk.defaultdict(dict)
    k=[]
    for w in range(len(brown_tg_words)-1):
        a=brown_tg_words[w]
        b=brown_tg_words[w+1]
        if a[0]==word and a[1]==tag:
            k+=[b[1]]
    dictop1[tag]=set(a)
    dictop2[word]=dictop1
    return dictop2
futuretag('go','VB')

    
            
        

