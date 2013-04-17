# fine
#
# TODO
# Comments?
# Two different for loops for creating fd? Why?

# Petrukha Tetiana Als-11
# Chapter_5, Ex_21

# In Table 3-1, we saw a table involving frequency counts for the verbs adore,
# love, like, and prefer, and preceding qualifiers such as really.
# Investigate the full range of qualifiers (Brown tag QL) that appear before these four verbs.

import nltk
fd = nltk.FreqDist() # frequency distribution
text=nltk.corpus.brown.words(categories='romance')
dic=['']
for (wd, tg) in nltk.corpus.brown.tagged_words():
	if tg[:2] == 'QL': # garner statistics about the tags
		fd.inc(wd)
verbs=['adore', 'love', 'like', 'prefer'] # list verbs
for i in range(len(text)):
	if text[i]in fd.keys()and text[i+1]in verbs and (text[i]+' '+text[i+1]) not in dic:
		dic.append(text[i]+' '+text[i+1]) # create a list of our verbs

print dic
