#work with tagger
#improve its performance
import nltk
from nltk.corpus import brown
patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*es$', 'VBZ'),
    (r'.*ed$', 'VBD'),
    (r'.*ould$', 'MD'),
    (r'.*s$', 'NNS'),
    (r'.*\'s$', 'NN$'),
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
    (r'.*', 'NN')
    ]
regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown.sents()[10])
print regexp_tagger.tag(brown.sents()[10])
brown_test=brown.tagged_sents()[:50]
100.0 * regexp_tagger.evaluate(brown.tagged_sents()[50:500])
print 100.0 * regexp_tagger.evaluate(brown.tagged_sents()[50:500])
two_tagger=nltk.UnigramTagger(brown_test, backoff=regexp_tagger)
100.0 * two_tagger.evaluate(brown.tagged_sents()[50:500])
print 100.0 * two_tagger.evaluate(brown.tagged_sents()[50:500])

         
