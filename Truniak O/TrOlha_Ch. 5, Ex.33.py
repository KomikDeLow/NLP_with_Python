# Presented by Olha Truniak, ALs-13
# Chapter 5, Ex.33

# Write code that builds a dictionary of dictionaries of sets. Use it to store the set
# of POS tags that can follow a given word having a given POS tag, i.e., wordi → tagi →
# tagi+1.

import nltk
slova=nltk.corpus.brown.tagged_words()
# I start to write a function, which can help me to store the set of POS tags
def futuretag(word, tag):
	zminna1=dict()
	zminna2=nltk.defaultdict(dict)
	a=[]
	for w in range(len(slova)-1):
		d=slova[w]
		c=slova[w+1]
		if d[0]==word and d[1]==tag: # The set of POS tags that can follow a given word having
                # a given POS tag as it is in my task
			a+=[c[1]]
	zminna1[tag]=set(a)
	zminna2[word]=zminna1
	return zminna2
# Building a dictionary of sets

futuretag('drink','VB')
futuretag('walk','VB')
futuretag('type','VB')
