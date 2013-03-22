# -*- coding: cp1251 -*-
import nltk
from nltk.corpus import floresta
print'Unigram tagger:'
floresta_tagged_sents=floresta.tagged_sents
floresta_sents=floresta.sents
unigram_tagger=nltk.UnigramTagger(floresta.tagged_sents())
unigram_tagger.tag(floresta.sents()[100])
print unigram_tagger.tag(floresta.sents()[100])# ��������� �������� unigram tagger, ��� ����������� ����� � ������� floresta
unigram_tagger.evaluate(floresta.tagged_sents()[:100])
print unigram_tagger.evaluate(floresta.tagged_sents()[:100])#� ����� ������ ���������� unigram tagger

from nltk.corpus import brown
brown_tagged_sents=brown.tagged_sents(categories='adventure')
brown_sents=brown.sents(categories='adventure')
unigram_tagger=nltk.UnigramTagger(brown.tagged_sents())
unigram_tagger.tag(brown.sents()[100])
print unigram_tagger.tag(brown.sents()[100])# ��������� �������� unigram tagger, ��� ����������� ����� � ������� brown
unigram_tagger.evaluate(brown.tagged_sents()[:100])
print unigram_tagger.evaluate(brown.tagged_sents()[:100])#� ����� ������ ���������� unigram tagger

print'Bigram tagger:'
#������������ bigram tagger ��� ���������� �� ������
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
#���������� ���������, �� unigram tagger �� ������ ������, ��� bigram tagger. �� ����� �������� ���, �� bigram tagger �������� ���� ��� ������, �� �� ����� �� ��� ��������, � �����-�.
#���� ���������� ������� unigram tagger �� ��������� floresta �� brown, �� ������� � ��������� ���������� ������� brown
