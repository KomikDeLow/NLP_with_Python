# -*- coding: cp1251 -*-
import nltk
from nltk.corpus import floresta
print'Unigram tagger:'
floresta_tagged_sents=floresta.tagged_sents
floresta_sents=floresta.sents
unigram_tagger=nltk.UnigramTagger(floresta.tagged_sents())
unigram_tagger.tag(floresta.sents()[100])
print unigram_tagger.tag(floresta.sents()[100])# проводимо навчання unigram tagger, щоб протагувати слова з корпусу floresta
unigram_tagger.evaluate(floresta.tagged_sents()[:100])
print unigram_tagger.evaluate(floresta.tagged_sents()[:100])#а також робимо оцінювання unigram tagger

from nltk.corpus import brown
brown_tagged_sents=brown.tagged_sents(categories='adventure')
brown_sents=brown.sents(categories='adventure')
unigram_tagger=nltk.UnigramTagger(brown.tagged_sents())
unigram_tagger.tag(brown.sents()[100])
print unigram_tagger.tag(brown.sents()[100])# проводимо навчання unigram tagger, щоб протагувати слова з корпусу brown
unigram_tagger.evaluate(brown.tagged_sents()[:100])
print unigram_tagger.evaluate(brown.tagged_sents()[:100])#а також робимо оцінювання unigram tagger

print'Bigram tagger:'
#використання bigram tagger для тренування та оцінки
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
#результати показують, що unigram tagger дає точнішу оцінку, аніж bigram tagger. Це можна пояснити тим, що bigram tagger призначає теги тим словам, які він бачив під час навчання, а іншим-ні.
#якщо порівнювати точність unigram tagger між корпусами floresta та brown, то точнішим є результат оцінювання корпусу brown
