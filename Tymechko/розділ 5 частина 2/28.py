import nltk
text=nltk.corpus.brown.tagged_words()
def nexttag(word, tag):
    vocab1=dict()
    vocab2=nltk.defaultdict(dict)
    a=[]
    for w in range(len(text)-1):
        d=text[w]
        c=text[w+1]
        if d[0]==word and d[1]==tag:
            a+=[c[1]]
    vocab1[tag]=set(a)
    vocab2[word]=vocab1
    return vocab2
print(nexttag('buy','VB'))
print(nexttag('close','VB'))
print(nexttag('fly','VB'))
