
# Building a dictionary in order: {[word]:{[tag(0)]:[tag(1)],[tag(1)]:[tag(2)],...,[tag(3)]:[tag(4)]}}


import nltk
from nltk.corpus import brown
brown_tg_words=brown.tagged_words(categories='news', simplify_tags=True)
ConFd = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_tg_words)
dictop1={}
dictop2={}
print 'Length of used words: ',len(ConFd)
for word in ConFd.conditions():
    if len(ConFd[word])==1:
        dictop1[ConFd[word].keys()[0]]='none'
        dictop2[word]=dictop1
        dictop1={}
    if len(ConFd[word])==2:
        dictop1[ConFd[word].keys()[0]]=ConFd[word].keys()[1]
        dictop2[word]=dictop1
        dictop1={}
    if len(ConFd[word])==3:
        for ind in range(2):
            dictop1[ConFd[word].keys()[ind]]=ConFd[word].keys()[ind+1]
        dictop2[word]=dictop1
        dictop1={}
    if len(ConFd[word])==4:
        for ind in range(3):
            dictop1[ConFd[word].keys()[ind]]=ConFd[word].keys()[ind+1]
        dictop2[word]=dictop1
        dictop1={}

print 'Length of bulded dictionary',len(dictop2)
print 'Main dictionari name "dictop2".'
