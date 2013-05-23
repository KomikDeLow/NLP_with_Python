# Constructing Regular Expresings chunker with the help of Conll2000 corpus and provided chunks lists of 'PP'

import nltk
from nltk.corpus import *

Colltrain_Words=conll2000.chunked_words('train.txt',chunk_types=['PP'])# Chunked data

tree_list=[]
tree_list=[w for w in Colltrain_Words if type(w)==nltk.tree.Tree] # Sorting a list containing only Tree type elements


list_for_FD=[]
for w in tree_list:
    list_for_FD.append(w.pprint()) # converting Tree type into STR for FreqDist
fd=nltk.FreqDist(list_for_FD)
keys_list=fd.keys()

print '10 most frequent PP Chunks:'
for w in range(10): # list of most frequent Chunks
    print keys_list[w]

dbl_key_list=[]
for word in keys_list: # list of Chunks consistion of more than 1 element
    counter=0
    for let in word:
        if let=='/':
            counter=counter+1
    if counter>1:
        dbl_key_list.append(word)

print '10 most frequent PP Chunks that have more than one component:'
for w in range(10):
    print dbl_key_list[w] # Providing the list of chunks consisting from more than one element

#In the next Line : Building a grammar for RegexpParset - Chunker
grammar_for_PP = r"""
PP: {<IN>?<JJ|RB|TO>?<IN>?}
    {</><CC>}
"""
cp=nltk.RegexpParser(grammar_for_PP)
Colltest_Sents=conll2000.chunked_sents('test.txt',chunk_types=['PP']) # Creating a test set for evaluation
print 'Evaluating the Chunker: '
print cp.evaluate(Colltest_Sents) # Evaluating the Chunker
