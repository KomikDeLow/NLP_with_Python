# TODO
# It isn't Python modul
# Data didn't divide on train and test part!
#
#

>>> import nltk
>>> from nltk.corpus import floresta
>>> from nltk.corpus import brown
>>> unigram_Portuguese = nltk.UnigramTagger(floresta.tagged_sents()[:1000])
>>> unigram_English = nltk.UnigramTagger(brown.tagged_sents()[:1000])
>>> unigram_Portuguese.evaluate(floresta.tagged_sents()[:1000])
0.8989380885594069
>>> unigram_English.evaluate(brown.tagged_sents()[:1000])
0.9482766429639023
>>> bigram_Portuguese = nltk.BigramTagger(floresta.tagged_sents()[:1000])
>>> bigram_Portuguese.evaluate(floresta.tagged_sents()[:1000])
0.6165497896213183
>>> bigram_English = nltk.BigramTagger(brown.tagged_sents()[:1000])
>>> bigram_English.evaluate(brown.tagged_sents()[:1000])
0.824176819602337
>>> trigram_Portuguese = nltk.TrigramTagger(floresta.tagged_sents()[:1000])
>>> trigram_Portuguese.evaluate(floresta.tagged_sents()[:1000])
0.6893608495291524
>>> trigram_English = nltk.TrigramTagger(brown.tagged_sents()[:1000])
>>> trigram_English.evaluate(brown.tagged_sents()[:1000])
0.8816975406494859

