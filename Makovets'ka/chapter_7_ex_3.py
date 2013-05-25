#Develop a simple chunker using the regular
#expression chunker nltk.RegexpParser

import nltk
from nltk.corpus import *
trainColl_Words=conll2000.chunked_words('train.txt',chunk_types=['PP'])

tree_list=[]
tree_list=[w for w in trainColl_Words if type(w)==nltk.tree.Tree] #Tree type elements

list_for_FD=[]
for w in tree_list:
    list_for_FD.append(w.pprint())
fd=nltk.FreqDist(list_for_FD)
keys_list=fd.keys()

print '10 most frequent PP Chunks:'
for w in range(10):
    print keys_list[w]

dbl_key_list=[]
for w in keys_list: # list of chunks consistion of more than one element
    counter=0
    for let in w:
         if let=='/':
             counter=counter+1
    if counter>1:
        dbl_key_list.append(w)

print '10 most frequent PP Chunks that have more than one component:'
for w in range(10):
    print dbl_key_list[w] # providing a list of chunks

grammar = r"""
PP: {<IN>?<JJ|RB|TO>?<IN>?}
{</><CC>}
"""
cp=nltk.RegexpParser(grammar) #building a grammar
testColl_Sents=conll2000.chunked_sents('test.txt',chunk_types=['PP'])
print 'Evaluating the Chunker that was builded: '
print cp.evaluate(testColl_Sents)
