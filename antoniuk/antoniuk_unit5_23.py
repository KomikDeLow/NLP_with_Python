# Prizvuscze / Grypa

import nltk
from nltk.corpus import brown
patterns = [
    (r'.*ing$', 'VBG'), 
    (r'.*ed$', 'VBP'), 
    (r'.*es$', 'VB3'), 
    (r'.*ould$', 'MD'), 
    (r'.*\'s$', 'NN$'), 
    (r'.*s$', 'NNP'), 
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), 
    (r'.*', 'NN') 
    ]
regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown.sents()[4])
[('The', 'NN'), ('jury', 'NN'), ('said', 'NN'), ('it', 'NN'), ('did', 'NN'), ('find', 'NN'),
 ('that', 'NN'), ('many', 'NN'), ('of', 'NN'), ("Georgia's", 'NN$'), ('registration', 'NN'),
 ('and', 'NN'), ('election', 'NN'), ('laws', 'NNP'), ('``', 'NN'), ('are', 'NN'),
 ('outmoded', 'VBP'), ('or', 'NN'), ('inadequate', 'NN'), ('and', 'NN'), ('often', 'NN'), ('ambiguous', 'NNP'), ("''", 'NN'), ('.', 'NN')]
brown_test=brown.tagged_sents()[:100]
print 'Regular expressions Tagger:'
print 'Accuracy: %4.1f%%' % (100.0 * regexp_tagger.evaluate(brown.tagged_sents()[100:1000]))


two_tagger=nltk.UnigramTagger(brown_test, backoff=regexp_tagger)
print 'Regular expressions Tagger + Unigram tagger:'
print 'Accuracy: %4.1f%%' % (100.0 * two_tagger.evaluate(brown.tagged_sents()[100:1000]))
# objective evaluation helps to improve our investigations