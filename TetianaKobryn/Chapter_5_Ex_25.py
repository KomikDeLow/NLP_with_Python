import nltk
from nltk.corpus import floresta
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
floresta_tagged_sents = nltk.corpus.floresta.sents()
size1 = int(len(brown_tagged_sents) * 0.9)
size2 = int(len(floresta_tagged_sents) * 0.9)
train_sents1 = brown_tagged_sents[:size1]
test_sents1 = brown_tagged_sents[size1:]
train_sents2 = floresta.tagged_sents()[:size2]
test_sents2 = floresta.tagged_sents()[size2:]
unigram_Portuguese = nltk.UnigramTagger(train_sents2)
unigram_English = nltk.UnigramTagger(train_sents1)
u2 = unigram_Portuguese.evaluate(test_sents2)
u1 = unigram_English.evaluate(test_sents1)

bigram_Portuguese = nltk.BigramTagger(train_sents2, backoff=unigram_Portuguese)
b2 = bigram_Portuguese.evaluate(test_sents2)
bigram_English = nltk.BigramTagger(train_sents1, backoff=unigram_English)
b1 = bigram_English.evaluate(test_sents1)

trigram_Portuguese = nltk.TrigramTagger(train_sents2, backoff=bigram_Portuguese)
t2 = trigram_Portuguese.evaluate(test_sents2)
trigram_English = nltk.TrigramTagger(train_sents1, backoff=bigram_English)
t1 = trigram_English.evaluate(test_sents1)

print 'trigram_English', t1
print 'trigram_Portuguese', t2
print 'bigram_English', b1
print 'bigram_Portuguese', b2
print 'unigram_English', u1
print 'unigram_Portuguese', u2

#trigram_English 0.817900926941
#trigram_Portuguese 0.788202969718
#bigram_English 0.820791388418
#bigram_Portuguese 0.79118437975
#unigram_English 0.811023622047
#unigram_Portuguese 0.766222378113
