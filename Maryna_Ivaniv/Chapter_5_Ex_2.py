#Ivaniv Maryna PRLs-11 Chapter 5 Ex.2
#Working with someone else, take turns picking a word that can be either a noun
#or a verb (e.g., contest); the opponent has to predict which one is likely to be the
#most frequent in the Brown Corpus. Check the opponent’s prediction, and tally
#the score over several turns.

import nltk
from nltk.corpus import brown
brown.categories()
fdist = nltk.FreqDist(brown.words(categories='adventure'))
most_freq_words= fdist.keys() #looking for the most commonly used words
cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='adventure'))#use FreqDist to check the frequency of tags
print 'address' in most_freq_words #if TRUE than the word is used in the text;if FALSE isn't used
print cfd ['address'].items()#the frequency of Nouns and Verbs in the text
print 'cover' in most_freq_words
print cfd ['cover'].items()
print 'face' in most_freq_words
print cfd ['face'].items()
print 'joke' in most_freq_words
print cfd ['joke'].items()
print 'jail' in most_freq_words
print cfd ['jail'].items()
# we can choose a word that can be either a noun
# or a verb and see their frequency in text.
#if TRUE than the word is used in the text;if FALSE isn't used
