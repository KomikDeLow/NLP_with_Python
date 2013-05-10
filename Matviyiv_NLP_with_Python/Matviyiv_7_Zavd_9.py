# TODO
# Please, describe me the algorithm of your solution
#
#


import nltk

from nltk.corpus import *

list_of_words_NP=conll2000.chunked_words('train.txt', chunk_types=['NP'])
list_of_trees_NP=[w for w in list_of_words_NP if type(w)==nltk.tree.Tree] # Building a list of all NP trees
print len(list_of_trees_NP), ': NP Trees among chunked words.'

tagged_words=brown.tagged_words()
tagged_words_conditional_freq=nltk.ConditionalFreqDist((word,tag)for(word,tag) # Building a Conditional FreqDist to separate words which are assigned only one tag
                                                       in tagged_words)
words_one_tag=[word for word in tagged_words_conditional_freq.conditions() # Building a list of words with only one tag
               if len(tagged_words_conditional_freq[word])==1]
NN_list=[w for w in tagged_words if w[1].startswith('NN')] # Building a list of Nouns
NN_list_set=set(NN_list) # Building a set of Nouns
NN_list_only_one_tag=[w for w in NN_list_set if w[0] in words_one_tag] # Building a list were all nouns are also words which are assigned only one tag

print len(NN_list_only_one_tag), ': Nouns in Brown corpus that are always assigned only one tag.'

NN_list_no_tag=[]
for w in NN_list_only_one_tag: # Building a list containing only words (no tags)
    NN_list_no_tag.append(w[0])

Tag_list=[] 
for w in NN_list_only_one_tag: # Building a list of only tags which are possible for Nouns
    Tag_list.append(w[1])
fd=nltk.FreqDist(Tag_list)
Tag_list_set=fd.keys() 

Error_list=[]
for w in list_of_trees_NP: # Procedure in wich we look for Trees containing Nouns from our List(of nouns which can have only one tag) and looking if the tag is not a Noun tag
    for word in w:
        if (word[0] in NN_list_no_tag) and (word[1] not in Tag_list_set):
            Error_list.append(w)

print len(Error_list), ':of:', len(list_of_trees_NP),': Number of Trees which can have mistakes in tagged Nouns.' # List containing the trees which may have an error

# Please do comment, becouse I dont know if this is correct.
