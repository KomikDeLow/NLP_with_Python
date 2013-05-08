# Daria Morozova
# Chapter 5 Ex. 11
# Corrected: The AffixTagger accuracy has been added


import nltk
from nltk.corpus import *
help(nltk.AffixTagger)
train_sents = [
[('Before','ADV'), ('giving','VG'), ('a','DET'), ('test','N'), ('the','DET')],
[('teacher','N'), ('should','MOD'), ('make','V'), ('sure','ADJ')],
[('that','CNJ'), ('the','DET'), ('students','N'), ('are','V'), ('prepared','VD')],
]
text = 'Otherwise they can fail the test.'
affix_tagger = nltk.AffixTagger(train_sents, affix_length=-2, min_stem_length=0)
tags = affix_tagger.tag(nltk.word_tokenize(text))
print tags
print 'Evaluation = ',affix_tagger.evaluate(train_sents)
affix_tagger.evaluate( train_sents)
affix_tagger = nltk.AffixTagger(train_sents, affix_length=-1, min_stem_length=2)
tags = affix_tagger.tag(nltk.word_tokenize(text))
print tags
print 'Evaluation = ',affix_tagger.evaluate(train_sents)
affix_tagger.evaluate( train_sents)
affix_tagger = nltk.AffixTagger(train_sents, affix_length=2, min_stem_length=2)
tags = affix_tagger.tag(nltk.word_tokenize(text))
print tags
affix_tagger.evaluate( train_sents)
print 'Evaluation = ',affix_tagger.evaluate(train_sents)
affix_tagger = nltk.AffixTagger(train_sents, affix_length=2, min_stem_length=5)
tags = affix_tagger.tag(nltk.word_tokenize(text))
print tags
affix_tagger.evaluate( train_sents)
print 'Evaluation = ',affix_tagger.evaluate(train_sents)

