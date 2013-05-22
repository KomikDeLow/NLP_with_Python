# TODO
# It isn't a Python modul
# Comments?
#


import nltk
from nltk.corpus import brown
fd=nltk.FreqDist(brown.words(categories='news'))
most_freq_words=fd.keys()
cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
print 'help' in most_freq_words
print cfd['help'].items()
print 'walk' in most_freq_words
print cfd['walk'].items()
print 'cat' in most_freq_words
print cfd['cat'].items()

