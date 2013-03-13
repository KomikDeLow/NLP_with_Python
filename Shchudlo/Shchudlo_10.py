import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print unigram_tagger.tag(['His', 'humorous', 'intention', 'to',
                    'describe', 'the', 'story', 'of', 'a', 'fictitious',
                    'trip', 'to', 'Mars', 'quickly', 'raised', 'eyebrows', 'as',
                    'his', 'Brooklyn,', 'New', 'York,', 'audience',
                    'grew', 'curious', 'about', 'what', 'life', 'was',
                    'like', 'on', 'the', 'red', 'planet', '.',
                    'Throughout', 'the', 'centuries,', 'people', 'indulged',
                    'their', 'fascination', 'about', 'life', 'on', 'Mars',
                    'through', 'the', 'imagination', 'of', 'artists', 'and',
                    'storytellers',',', 'as', 'well', 'as', 'through', 'the',
                    'lens', 'of', 'telescopes', 'that', 'returned', 'imprecise',
                    'images','.'])
print 'Evaluation = ' ,unigram_tagger.evaluate(brown_tagged_sents)