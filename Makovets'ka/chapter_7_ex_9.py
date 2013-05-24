#Sometimes a word is incorrectly tagged, e.g.,
#the head noun in 12/CD or/CC so/
#RB cases/VBZ. Instead of requiring manual
#correction of tagger output, good
#chunkers are able to work with the erroneous output of taggers
#look for other examples of correctly chunked
#noun phrases with incorrect tags

import nltk
from nltk.corpus import *
list_of_words_NP=conll2000.chunked_words('train.txt', chunk_types=['NP'])
list_of_trees_NP=[w for w in list_of_words_NP if type(w)==nltk.tree.Tree]
print len(list_of_trees_NP), ': NP Trees among chunked words.'
tagged_words=brown.tagged_words()
tagged_words_conditional_freq=nltk.ConditionalFreqDist((word,tag)for(word,tag)
                                                       in tagged_words)
words_one_tag=[word for word in tagged_words_conditional_freq.conditions()
               if len(tagged_words_conditional_freq[word])==1]
NN_list=[w for w in tagged_words if w[1].startswith('NN')] #spysok imennykiv
NN_list_set=set(NN_list)
NN_list_only_one_tag=[w for w in NN_list_set if w[0] in words_one_tag]
print len(NN_list_only_one_tag), ': Nouns in Brown corpus that are always assigned only one tag.'
NN_list_no_tag=[]
for w in NN_list_only_one_tag:
    NN_list_no_tag.append(w[0]) #spysok bez tegiv
Tag_list=[]
for w in NN_list_only_one_tag: #spysok tegiv
    Tag_list.append(w[1])
fd=nltk.FreqDist(Tag_list)
Tag_list_set=fd.keys()
Error_list=[]
for w in list_of_trees_NP:
    for word in w:
        if (word[0] in NN_list_no_tag) and (word[1] not in Tag_list_set):
            Error_list.append(w)


print len(Error_list), ':of:', len(list_of_trees_NP),': Number of Trees which can have mistakes in tagged Nouns.'
                                                       
