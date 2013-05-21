# Oleniuk Roksolana
# PRLs-12
# Chapter 5 Ex. 8


import nltk
e = nltk.defaultdict(list)
def dic(headword,part_of_speech,sense,example):
    e[headword]=[part_of_speech,sense,example]
e=('moustache','N','The unshaved growth of hair on the upper lip, and sometimes down the sides of the mouth.')
print e 	
