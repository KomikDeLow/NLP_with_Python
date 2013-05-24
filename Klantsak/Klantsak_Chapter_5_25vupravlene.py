#Veronika Klantsak ALs-11

#Evaluation and training Unigram tagger and Bigram tagger 

import nltk
from nltk.corpus import floresta
print'Unigram tagger:'
floresta_tagged_sents=floresta.tagged_sents
floresta_sents=floresta.sents
unigram_tagger=nltk.UnigramTagger(floresta.tagged_sents())
unigram_tagger.tag(floresta.sents()[100])
# provodumo navchannya unigram tagger, shchob protagyvatu slova z korpysy floresta:
print unigram_tagger.tag(floresta.sents()[100])
unigram_tagger.evaluate(floresta.tagged_sents()[:100])
# ocinyuvannya unigram tagger:
print unigram_tagger.evaluate(floresta.tagged_sents()[:100])
from nltk.corpus import brown
brown_tagged_sents=brown.tagged_sents(categories='adventure')
brown_sents=brown.sents(categories='adventure')
unigram_tagger=nltk.UnigramTagger(brown.tagged_sents())
unigram_tagger.tag(brown.sents()[100])
# provodumo navchannya unigram tagger, shchob protagyvatu slova z korpysy brown:
print unigram_tagger.tag(brown.sents()[100])
unigram_tagger.evaluate(brown.tagged_sents()[:100])
# ocinyuvannya unigram tagger:
print unigram_tagger.evaluate(brown.tagged_sents()[:100])

print'Bigram tagger:'
#vukorustannya bigram tagger dlya trenyvannya ta ocinku
bigram_tagger=nltk.BigramTagger(floresta.tagged_sents())
bigram_tagger.tag(floresta.sents()[100])
print bigram_tagger.tag(floresta.sents()[100])
bigram_tagger.evaluate(floresta.tagged_sents()[:100])
print bigram_tagger.evaluate(floresta.tagged_sents()[:100])
bigram_tagger=nltk.BigramTagger(brown.tagged_sents())
bigram_tagger.tag(brown.sents()[100])
print bigram_tagger.tag(brown.sents()[100])
bigram_tagger.evaluate(brown.tagged_sents()[:100])
print bigram_tagger.evaluate(brown.tagged_sents()[:100])
# rezyl'tatu pokazyyut', shcho unigram tagger dae tochniwy ocinky, nizh bigram tagger. Ce mozhna poyasnutu tum, shchо bigram tagger pruznachae tegu tum slovam,taki vin bachuv pid chas navchannya, a inwum -ni.
# Yakwo porivnyuvatu tochnist' unigram tagger mizh korpysamu floresta та brown, to tochniwum e rezyl'tat ocinyuvannya korpysy brown.
