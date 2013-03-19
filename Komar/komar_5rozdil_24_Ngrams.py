# TODO
# Comments?
# What does your program do?
# The train data and test data are identical. Why?
import nltk
from nltk.corpus import brown
for i in range (1,6):
	n_grams = nltk.NgramTagger (i,nltk.corpus.brown.tagged_sents()[:10000])
	print n_grams.evaluate(nltk.corpus.brown.tagged_sents()[:10000])
