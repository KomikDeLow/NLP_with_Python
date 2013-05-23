#Write code that builds
#dictionary of dictionaries of sets.
#Use it to store
#the set of POS tags
#that can follow
#a given word having
#a given POS tag, i.e.,
#wordi → tagi → tagi+1.

import nltk
brown_tagged=nltk.corpus.brown.tagged_words()
def tag(word,tag):
    w=dict()
    a=nltk.defaultdict(dict)
    c=[]
    for i in range(len(brown_tagged)-1):
        d=brown_tagged[i]
        e=brown_tagged[i+1]
        if d[0]==word and d[1]==tag:
            c+=[e[1]]
    w[tag]=set(c)
    a[word]=w
    return a
tag('moon','NN')
print tag('moon','NN')
