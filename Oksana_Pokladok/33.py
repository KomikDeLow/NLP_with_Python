import nltk
from nltk.corpus import brown
br=nltk.corpus.brown.tagged_words()
def findme (word, tag):
    w=dict()
    a=nltk.defaultdict(dict)
    c=[]
    for i in range (len(br)-1):
        d=br[i]
        e=br[i+1]
        if d[0]==word and d[1]==tag:
            c+=[e[1]]
            w[tag]=set(c)
            a[word]=w
            return a

print findme('book','NN') 
print findme('help','NN')
print findme('a','AT')
