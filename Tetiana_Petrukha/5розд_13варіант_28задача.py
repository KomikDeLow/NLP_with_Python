# TODO
# Comments?
# I didn't see answer

# Petrukha Tetiana Als-11
# Chapter_5, Ex_28

# Experiment with taggers using the simplified tagset.
# Such a tagger has fewer distinctions to make, but much less information on
# which to base its work. Discuss your findings.

import nltk
st = nltk.corpus.treebank.tagged_words(simplify_tags=True) # here we are using the simplified tagset
word_tag_fd = nltk.FreqDist(st) # frequency distribution
noun=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('N')] # sort all the noun by frequency
print noun[:20] # print noun
print('')
nst = nltk.corpus.treebank.tagged_words(simplify_tags=False) # here we aren't using the simplified tagset
word_tag_fd = nltk.FreqDist(nst)
us_noun=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('N')]
print us_noun [:20]

# Not all corpora employ the same set of tags. If we want to avoid the complications
# of these tagsets, so we use a built-in mapping to a simplified tagset
# But they are much less informative.
# For example we take a nouns tags. At bouth tagset(Simplified and Unsimplified)
# we can see plural nouns-NS or proper nouns-NP
# But Simplified tagset don't have suffix modifiers: -NC for citations,
# -HL for words in headlines, and -TL for titles 
