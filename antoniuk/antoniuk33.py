import nltk
brown_tagged=nltk.corpus.brown.tagged_words()
def tag(word,tag):
    w=dictionary()
    a=nltk.defaultdict(dictionary)
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
