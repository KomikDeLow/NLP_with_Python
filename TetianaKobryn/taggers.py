# TODO
# Comments?
# How work your program?
#

#Presented by Tetiana Kobryn

#Chapter 5, Ex.25
#
#Obtain some tagged data for another language, and train and evaluate a variety
#of taggers on it. If the language is morphologically complex, or if there are
#any orthographic clues (e.g., capitalization) to word classes, consider
#developing a regular expression tagger for it (ordered after the unigram tagger,
#and before the default tagger). How does the accuracy of your tagger(s) compare
#with the same taggers run on English data? Discuss any issues you encounter in
#applying these methods to the language.

import nltk
from nltk.corpus import floresta
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
floresta_tagged_sents = nltk.corpus.floresta.sents()
#split the data, training on 90% and testing on the remaining 10%
size1 = int(len(brown_tagged_sents) * 0.9)
size2 = int(len(floresta_tagged_sents) * 0.9)
train_sents1 = brown_tagged_sents[:size1]
test_sents1 = brown_tagged_sents[size1:]
train_sents2 = floresta.tagged_sents()[:size2]
test_sents2 = floresta.tagged_sents()[size2:]
#train a UnigramTagger for Portuguese and English
unigram_Portuguese = nltk.UnigramTagger(train_sents2)
unigram_English = nltk.UnigramTagger(train_sents1)
#evaluate the performance of UnigramTagger for Portuguese and English
u2 = unigram_Portuguese.evaluate(test_sents2)
u1 = unigram_English.evaluate(test_sents1)
#train a BigramTagger for Portuguese and English
bigram_Portuguese = nltk.BigramTagger(train_sents2, backoff=unigram_Portuguese)
b2 = bigram_Portuguese.evaluate(test_sents2)
bigram_English = nltk.BigramTagger(train_sents1, backoff=unigram_English)
#evaluate the performance of BigramTagger for Portuguese and English
b2 = bigram_Portuguese.evaluate(test_sents2)
b1 = bigram_English.evaluate(test_sents1)
#train a TrigramTagger for Portuguese and English
trigram_Portuguese = nltk.TrigramTagger(train_sents2, backoff=bigram_Portuguese)
trigram_English = nltk.TrigramTagger(train_sents1, backoff=bigram_English)
#evaluate the performance of TrigramTagger for Portuguese and English
t2 = trigram_Portuguese.evaluate(test_sents2)
t1 = trigram_English.evaluate(test_sents1)

#present results
print 'trigram_English', t1
print 'trigram_Portuguese', t2
print 'bigram_English', b1
print 'bigram_Portuguese', b2
print 'unigram_English', u1
print 'unigram_Portuguese', u2

print "The accuracy of Portuguese tagger is worse than of English"
