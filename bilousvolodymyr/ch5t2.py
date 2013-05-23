# Bilous Volodymyr, AL-11
#chapter 5, task 2
import nltk
from nltk.corpus import brown
fd = nltk.FreqDist(brown.words(categories = 'news'))
freq_words= fd.keys()
cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
print 'access' in freq_words
print cfd ['access'].items()
print 'blame' in freq_words
print cfd ['blame'].items()
print 'crush' in freq_words
print cfd ['crush'].items()
print 'demand' in freq_words
print cfd ['demand'].items()
print 'fight' in freq_words
print cfd ['fight'].items()
print 'grin' in freq_words
print cfd ['grin'].items()
print 'land' in freq_words
print cfd ['land'].items()
print 'match' in freq_words
print cfd ['match'].items()
print 'play' in freq_words
print cfd ['play'].items()
print 'support' in freq_words
print cfd ['support'].items()
# We define if a word is a noun or a verb and observe the frequency of it.
# E.g. the word 'play' in the text is used 30 times as a verb and 11 times as a noun.
