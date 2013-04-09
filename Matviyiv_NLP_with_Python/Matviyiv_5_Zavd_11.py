#TODO
#You must divide data on train and test
#
#  Training an Affix Tagger and running it on some new text.
import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
train_data=brown_tagged_sents[:4000]
test_data=brown_tagged_sents[4000:]

aff_tagger=nltk.AffixTagger(train_data)
print aff_tagger.tag(['In', 'this', 'section,', 'you', 'can', 'practise', 'your',
                      'reading', 'skills.', 'It', 'contains', 'simplified', 'English',
                      'texts', 'which', 'are', 'written', 'in', 'easy', 'grammar,', 'so',
                      'that', 'students', 'of', 'pre-intermediate', 'level', 'can', 'easily',
                      'understand.', 'Have', 'fun', 'and', 'enjoy', 'your', 'reading'])


print '==============================================================='
print 'Affix tagger size = ',aff_tagger.size()
print 'Sentences used to evaluete = ',len(test_data)
print 'Evaluation = ',aff_tagger.evaluate(test_data)
print '==============================================================='


aff_tagger=nltk.AffixTagger(train_data,affix_length=-2)
print aff_tagger.tag(['In', 'this', 'section,', 'you', 'can', 'practise', 'your',
                      'reading', 'skills.', 'It', 'contains', 'simplified', 'English',
                      'texts', 'which', 'are', 'written', 'in', 'easy', 'grammar,', 'so',
                      'that', 'students', 'of', 'pre-intermediate', 'level', 'can', 'easily',
                      'understand.', 'Have', 'fun', 'and', 'enjoy', 'your', 'reading'])
print '==============================================================='
print 'Affix length changed to = -2 ','Affix tagger size = ',aff_tagger.size()
print 'Sentences used to evaluete = ',len(test_data)
print 'Evaluation = ',aff_tagger.evaluate(test_data)
print '==============================================================='


aff_tagger=nltk.AffixTagger(train_data,min_stem_length=4)
print aff_tagger.tag(['In', 'this', 'section,', 'you', 'can', 'practise', 'your',
                      'reading', 'skills.', 'It', 'contains', 'simplified', 'English',
                      'texts', 'which', 'are', 'written', 'in', 'easy', 'grammar,', 'so',
                      'that', 'students', 'of', 'pre-intermediate', 'level', 'can', 'easily',
                      'understand.', 'Have', 'fun', 'and', 'enjoy', 'your', 'reading'])
print '==============================================================='
print 'Minimum stem length changed to = 4 ','Affix tagger size = ',aff_tagger.size()
print 'Sentences used to evaluete = ',len(test_data)
print 'Evaluation = ',aff_tagger.evaluate(test_data)
print '==============================================================='
