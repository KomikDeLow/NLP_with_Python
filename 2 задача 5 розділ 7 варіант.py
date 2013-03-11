iimport nltk
from nltk.corpus import brown
fd=nltk.FreqDist(brown.words(categories='news'))
most_freq_words=fd.keys()
cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
print 'mother' in most_freq_words
print cfd['mother'].items()
print 'letter' in most_freq_words
print cfd['letter'].items()
print 'tree' in most_freq_words
print cfd['tree'].items()
