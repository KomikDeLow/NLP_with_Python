# fine but why does the precosion is low 
#
# TODO
# Comments?
# test and train data?

# Changing low-frequency words with UNK, but leaving the tags as they are, then evaluating the classifiers
# to see if this gave something to the accuracy.
import nltk
from nltk.corpus import brown
words_tagged=brown.tagged_words(categories='news')
fd=nltk.FreqDist(words_tagged) # building a frequency list of the used words
word_list=fd.keys() # building a set of words 
word_list.reverse() # reversing this set
words_to_change=word_list[:3000] # taking out 3000 low-frequency words
words_to_change_list=[]
for w in words_to_change:
	words_to_change_list.append(w[0]) # building a cycle to take out words without their tags

sents_train_for_cycle=brown.tagged_sents(categories='news')[:4000]

sent_with_changes=[]
sent_one=[]
counter=0
for sent in sents_train_for_cycle: # building a cycle which returns sentenses with changed low-frequency words to UNK
	for word in sent:
		if word[0] in words_to_change_list:
			sent_one.append(('UNK',word[1]))
			counter=counter+1
		else:
			sent_one.append(word)
	sent_with_changes.append(sent_one)
	sent_one=[]

sents_train=sents_train_for_cycle[:3000] # dividing data to train and test wich has no changed words
sents_test=sents_train_for_cycle[3000:]

sent_with_changes_train=sent_with_changes[:3000] # dividing data with changed words
sent_with_changes_test=sent_with_changes[3000:]

print counter,' words were changed to UNK in training sentences.'

Bigram_tagger=nltk.BigramTagger(sents_train) # Training taggers
Bigram_tagger_with_changes=nltk.BigramTagger(sent_with_changes_train)

print 'Accuracy Bigram_tagger (with normal unchanged words): %4.1f%%' % (
    100.0 * Bigram_tagger.evaluate(sents_test)) # Evaluating taggers
print 'Accuracy Bigram_tagger_with_changes (with changed low-frequency words): %4.1f%%' % (
    100.0 * Bigram_tagger_with_changes.evaluate(sent_with_changes_test))


Unigram_tagger=nltk.UnigramTagger(sents_train) # Training taggers
Unigram_tagger_with_changes=nltk.UnigramTagger(sent_with_changes_train)


print 'Accuracy Unigram_tagger (with normal unchanged words): %4.1f%%' % (
    100.0 * Unigram_tagger.evaluate(sents_test)) # Evaluating taggers
print 'Accuracy Unigram_tagger_with_changes (with changed low-frequency words): %4.1f%%' % (
    100.0 * Unigram_tagger_with_changes.evaluate(sent_with_changes_test))


