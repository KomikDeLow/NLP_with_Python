#TODO
#Why you didn't divide date on train date and test date
#
import nltk
from nltk.corpus import *
Unigram_English=nltk.UnigramTagger(brown.tagged_sents()[:1000])
Unigram_Brazilian=nltk.UnigramTagger(mac_morpho.tagged_sents()[:1000])

Unigram_English.tag(brown.sents()[9])
print 'Accuracy of Unigram tagger in English: %4.1f%%' % (
    100.0 * Unigram_English.evaluate(brown.tagged_sents()[:1000]))

Unigram_Brazilian.tag(mac_morpho.sents()[9])
print 'Accuracy of Unigram tagger in Brazilian(Brazilian Portuguese): %4.1f%%' % (
    100.0 * Unigram_Brazilian.evaluate(mac_morpho.tagged_sents()[:1000]))

Bigram_tagger_English=nltk.BigramTagger(brown.tagged_sents()[:1000])
Bigram_tagger_English.tag(brown.sents()[9])
print 'Accuracy of Bigram tagger in English: %4.1f%%' % (
    100.0 * Bigram_tagger_English.evaluate(brown.tagged_sents()[:1000]))

Bigram_tagger_Brazilian=nltk.BigramTagger(mac_morpho.tagged_sents()[:1000])
Bigram_tagger_Brazilian.tag(mac_morpho.sents()[9])
print 'Accuracy of Bigram tagger in Brazilian(Brazilian Portuguese): %4.1f%%' % (
    100.0 * Unigram_Brazilian.evaluate(mac_morpho.tagged_sents()[:1000]))
