#TODO
#Why you didn't divide date on train date and test date?
#
import nltk
from nltk.corpus import *
test_data1=brown.tagged_sents()[:1000]
train_data1=brown.tagged_sents()[1000:9000]

Braz_test_data1=mac_morpho.tagged_sents()[:1000]
Braz_train_data1=mac_morpho.tagged_sents()[1000:9000]

Unigram_English=nltk.UnigramTagger(train_data1)
Unigram_Brazilian=nltk.UnigramTagger(Braz_train_data1)

Unigram_English.tag(brown.sents()[9])
print 'Accuracy of Unigram tagger in English: %4.1f%%' % (
    100.0 * Unigram_English.evaluate(test_data1))

Unigram_Brazilian.tag(mac_morpho.sents()[9])
print 'Accuracy of Unigram tagger in Brazilian(Brazilian Portuguese): %4.1f%%' % (
    100.0 * Unigram_Brazilian.evaluate(Braz_test_data1))
    
test_data2=brown.tagged_sents()[9000:10000]
train_data2=brown.tagged_sents()[10000:19000]

Braz_test_data2=mac_morpho.tagged_sents()[9000:10000]
Braz_train_data2=mac_morpho.tagged_sents()[10000:19000]

Bigram_tagger_English=nltk.BigramTagger(train_data2)
Bigram_tagger_English.tag(brown.sents()[9])
print 'Accuracy of Bigram tagger in English: %4.1f%%' % (
    100.0 * Bigram_tagger_English.evaluate(test_data2))

Bigram_tagger_Brazilian=nltk.BigramTagger(Braz_train_data2)
Bigram_tagger_Brazilian.tag(mac_morpho.sents()[9])
print 'Accuracy of Bigram tagger in Brazilian(Brazilian Portuguese): %4.1f%%' % (
    100.0 * Unigram_Brazilian.evaluate(Braz_test_data2))
