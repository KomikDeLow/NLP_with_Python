#Presented by Tetiana Kobryn
#
#Chapter 5, Ex.15a
#a. Which nouns are more common in their plural form, rather than their singular
#form? (Only consider regular plurals, formed with the -s suffix.)

import nltk
from nltk.corpus import brown

#initializing empty lists
nouns=[]
singular=[]
plural=[]

#filling list of nouns
for (w,t) in brown.tagged_words(categories='news'): 
	if t.startswith('NN'):
		nouns.append(w)

#creating a frequency distribution containing list of nouns
fdistnoun = nltk.FreqDist(nouns)

#filling list of singular nouns		
for (w,t) in brown.tagged_words(categories='news'): 
	if t=='NN':
		singular.append(w)

#creating a frequency distribution containing list of singular nouns
fdistsg = nltk.FreqDist(singular)

#filling list of plural nouns, but without last letter
for (w,t) in brown.tagged_words(categories='news'): 
	if t=='NNS':
		plural.append(w[:-1])

#creating a frequency distribution containing list of plural nouns
fdistpl = nltk.FreqDist(plural)

#defining nouns that are more common in their plural form
for i in fdistnoun.keys():	
	if fdistpl[i]>fdistsg[i]:
		print i
