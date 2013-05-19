# Presented by Olha Truniak, ALs-13
# Chapter 5, Ex.2

import nltk
from nltk.corpus import brown
tr = nltk.FreqDist(brown.words(categories = 'news'))
freq_words= tr.keys()# Start up to find more frequent words
cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))# I put True if the word is present in the text and if it don't - False
# Print on a screen the frequency of those words
print 'set' in freq_words
print cfd ['set'].items()
print 'dance' in freq_words
print cfd ['dance'].items()
print 'look' in freq_words
print cfd ['look'].items()
print 'cut' in freq_words
print cfd ['cut'].items()
print 'smell' in freq_words
print cfd ['smell'].items()
print 'fly' in freq_words
print cfd ['fly'].items()
print 'book' in freq_words
print cfd ['book'].items()
# I check these words and explore their frequency.
# For example, the word SET is more frequent in using as VERB - 56 times,and as NOUN - only 1 time.

