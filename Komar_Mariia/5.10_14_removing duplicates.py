# fine
# TODO
# Why do you do sorted(set(tag_fd.keys())) twice ?

# Komar Mariia Als-11
# Chapter_6, Ex_14 

# Use sorted() and set() to get a sorted list of tags used in the Brown Corpus,
# removing duplicates.

import nltk
from nltk.corpus import brown
brown_tagged=brown.tagged_words() # create analyser with full set of tags
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_tagged)#create frequency distribution
sorted(set(tag_fd.keys())) #remove duplicates
print sorted(set(tag_fd.keys()))# print results
