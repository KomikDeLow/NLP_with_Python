# Komar Mariia Als-11, Ex_10 Chapter_5 
# Train a unigram tagger and run it on some new text.
# Observe that some words are not assigned a tag. Why not?

# Some words are not assigned a tag,
# becouse these words are not stored inside the tagger.

import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print unigram_tagger.tag(['I', 'like', 'this', 'wristwatch'])# print tagged sentence
