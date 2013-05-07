Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.corpus import brown
>>> from nltk.corpus import mac_morpho
>>> brown_tagged_sents = brown.tagged_sents(categories='editorial')
>>> mac_morpho_tagged_sents = nltk.corpus.mac_morpho.sents()
>>> train_sents1 = brown_tagged_sents[:1000]
>>> test_sents1 = brown_tagged_sents[1000:3000]
>>> train_sents2 = mac_morpho.tagged_sents()[:1000]
>>> test_sents2 = mac_morpho.tagged_sents()[1000:3000]
>>> unigram_English = nltk.UnigramTagger(train_sents1)
>>> unigram_Brazilian_Portugese = nltk.UnigramTagger(train_sents2)
>>> u1 = unigram_English.evaluate(test_sents1)
>>> u2 = unigram_Brazilian_Portugese.evaluate(test_sents2)
>>> bigram_English = nltk.BigramTagger(train_sents1, backoff=unigram_English)
>>> bigram_Brazilian_Portugese = nltk.BigramTagger(train_sents2, backoff=unigram_Brazilian_Portugese)
>>> b1 = bigram_English.evaluate(test_sents1)
>>> b2 = bigram_Brazilian_Portugese.evaluate(test_sents2)
>>> trigram_English = nltk.TrigramTagger(train_sents1, backoff=bigram_English)
>>> trigram_Brazilian_Portugese = nltk.TrigramTagger(train_sents2, backoff=bigram_Brazilian_Portugese)
>>> t1 = trigram_English.evaluate(test_sents1)
>>> t2 = trigram_Brazilian_Portugese.evaluate(test_sents2)
>>> print 'unigram_English', u1
unigram_English 0.731454151909
>>> print 'unigram_Brazilian_Portugese', u2
unigram_Brazilian_Portugese 0.708836321676
>>> print 'bigram_English', b1
bigram_English 0.737873868556
>>> print 'bigram_Brazilian_Portugese', b2
bigram_Brazilian_Portugese 0.721951003018
>>> print 'trigram_English', t1
trigram_English 0.737062180244
>>> print 'trigram_Brazilian_Portugese', t2
trigram_Brazilian_Portugese 0.72299396414
#I trained and evaluated unigram, bigram, and trigram taggers on the Brown (English language) and Mac_morpho (Brazilian Portugese) corpora. All these taggers work slightly better with English data.   
>>> 
