# Uliana Chubko AL-12
import nltk
from nltk.corpus import brown
patterns = [
    (r'.*\'s$', 'NN$'),# присвійні іменники
     (r'.*s$', 'NNS'),# іменники множини
    (r'.*', 'NN'),# іменники 
     (r'.*er', 'JJR'),# прикметники вищого ступеня
    (r'.*est', 'JJT'),# прикметники найвищого ступеня порівняння
    (r'.*ly', 'JJT'),# прислівники
     (r'.*dom', 'NNC'),# іменники однини та збірні іменники
     (r"NP: {<[CDJNP].*>+}"),# правила для типових іменникових фраз
    ]
regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown.sents()[15])
brown_test=brown.tagged_sents()[:150]
print 'RegexpTagger:'
print 'Accuracy:', regexp_tagger.evaluate(brown.tagged_sents()[150:1000])
#  для більшої точності використовуємо юніграми, бінрами, триграми з  RegexpTagger
unigram_chunker = nltk.UnigramTagger(brown_test, backoff=regexp_tagger)
bigram_chunker = nltk.BigramTagger(brown_test, backoff=unigram_chunker)
trigram_chunker=nltk.TrigramTagger(brown_test, backoff=bigram_chunker)
print 'RegexpTagger + Trigram tagger:'
print 'Accuracy:', trigram_chunker.evaluate(brown.tagged_sents()[150:1000])
 
