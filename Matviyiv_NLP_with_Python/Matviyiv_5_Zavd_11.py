#TODO
#You must divide data on train and test
#
import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
aff_tagger=nltk.AffixTagger(brown_tagged_sents)
print aff_tagger.tag(['In', 'this', 'section,', 'you', 'can', 'practise', 'your',
                      'reading', 'skills.', 'It', 'contains', 'simplified', 'English',
                      'texts', 'which', 'are', 'written', 'in', 'easy', 'grammar,', 'so',
                      'that', 'students', 'of', 'pre-intermediate', 'level', 'can', 'easily',
                      'understand.', 'Have', 'fun', 'and', 'enjoy', 'your', 'reading'])
print '==============================================================='
print 'Affix tagger size = ',aff_tagger.size()
print 'Sentences used to evaluete = ',len(brown.tagged_sents()[:1000])
print 'Evaluation = ',aff_tagger.evaluate(brown.tagged_sents()[:1000])
print '==============================================================='

brown_tagged_sents = brown.tagged_sents(categories='news')
aff_tagger=nltk.AffixTagger(brown_tagged_sents,affix_length=-2)
print aff_tagger.tag(['In', 'this', 'section,', 'you', 'can', 'practise', 'your',
                      'reading', 'skills.', 'It', 'contains', 'simplified', 'English',
                      'texts', 'which', 'are', 'written', 'in', 'easy', 'grammar,', 'so',
                      'that', 'students', 'of', 'pre-intermediate', 'level', 'can', 'easily',
                      'understand.', 'Have', 'fun', 'and', 'enjoy', 'your', 'reading'])
print '==============================================================='
print 'Affix length changed to = -2 ','Affix tagger size = ',aff_tagger.size()
print 'Sentences used to evaluete = ',len(brown.tagged_sents()[:1000])
print 'Evaluation = ',aff_tagger.evaluate(brown.tagged_sents()[:1000])
print '==============================================================='

brown_tagged_sents = brown.tagged_sents(categories='news')
aff_tagger=nltk.AffixTagger(brown_tagged_sents,min_stem_length=4)
print aff_tagger.tag(['In', 'this', 'section,', 'you', 'can', 'practise', 'your',
                      'reading', 'skills.', 'It', 'contains', 'simplified', 'English',
                      'texts', 'which', 'are', 'written', 'in', 'easy', 'grammar,', 'so',
                      'that', 'students', 'of', 'pre-intermediate', 'level', 'can', 'easily',
                      'understand.', 'Have', 'fun', 'and', 'enjoy', 'your', 'reading'])
print '==============================================================='
print 'Minimum stem length changed to = 4 ','Affix tagger size = ',aff_tagger.size()
print 'Sentences used to evaluete = ',len(brown.tagged_sents()[:1000])
print 'Evaluation = ',aff_tagger.evaluate(brown.tagged_sents()[:1000])
print '==============================================================='
