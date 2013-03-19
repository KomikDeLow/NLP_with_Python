# TODO
# Bad modul name
# Train and test dates are identical
# -*- coding: cp1251 -*-
#Shtanhret Iryna AL-13, zadacha 24
import nltk
from nltk.corpus import brown
brown_news_tagged=brown.tagged_sents(categories='news', simplify_tags=True)
test=brown.sents(categories='news')
for n in range (6):
	ngram=nltk.NgramTagger(n, brown_news_tagged)
	ngram.tag(test[3])
	print ngram.evaluate(brown_news_tagged)#побудувала цикл з н-грам тегів від 1-6 та оцінила через функцію евалуейт результати

