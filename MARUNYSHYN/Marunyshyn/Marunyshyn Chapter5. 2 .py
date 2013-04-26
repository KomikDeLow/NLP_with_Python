#Irena Marunyshyn PRLs-12 Chapter 5 EX2
# Working with someone else, take turns picking a word that can be either a noun
#or a verb (e.g., contest); the opponent has to predict which one is likely to be the
#most frequent in the Brown Corpus. Check the opponent’s prediction, and tally
#the score over several turns.
import nltk
from nltk.corpus import brown
fd = nltk.FreqDist(brown.words(categories = 'news'))
most_freq_words= fd.keys()# searching the most frequent words
cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))#use FreqDist to examine the frequency of tags
print 'contest' in most_freq_words# True - there is a word in our text, false - there is no word in text
print cfd ['contest'].items()#  the frequency of the word as a noun or verb
print 'effect' in most_freq_words
print cfd ['effect'].items()
print 'answer' in most_freq_words
print cfd ['answer'].items()
print 'address' in most_freq_words
print cfd ['address'].items()
print 'finish' in most_freq_words
print cfd ['finish'].items()
print 'fly' in most_freq_words
print cfd ['fly'].items()
print 'kiss' in most_freq_words
print cfd ['kiss'].items()
# we can pick a word that can be either a noun
# or a verb and see the frequency of the word which could be used as noun or verb in text.
# if there is no word in our text that it is false. if there is the word that -true.
# for examlpe, the word finish is true and used 2 times as noun and 1 time as verb.

