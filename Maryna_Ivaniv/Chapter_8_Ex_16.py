# Maryna Ivaniv PRLs-11 Chapter 8, Ex.16
# Write a program to find those verbs in the PP Attachment Corpus nltk.corpus.ppattach.
# Find any cases where the same verb exhibits two different attachments,
# but where the first noun, or second noun, or preposition stays unchanged
#(as we saw in our discussion of syntactic ambiguity in Section 8.2).

import nltk
entries = nltk.corpus.ppattach.attachments('training') 
table = nltk.defaultdict(lambda: nltk.defaultdict(set)) # empty dictionary,values ​​of his entries  are dictionaries

# choice of verb determines whether the prepositional phrase is attached to the VP or to the NP.	
for entry in entries:
    key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2 # fill the dictionary by keys that will contain a noun+preposition+noun
    table[key][entry.attachment].add(entry.verb)

# review vocabulary and text output
for key in sorted(table):
    if len(table[key]) > 1:
        print key, 'N:', sorted(table[key]['N']), 'V:', sorted(table[key]['V'])

# with the help of this program we can find different groups of words which have construction Noun+ prepositon+ noun
# and also the words constraction which are unchangeble. also I find unchangeble construction as stance-in-light. 

