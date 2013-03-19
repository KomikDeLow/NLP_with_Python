# TODO
# Is it the Python modul? No!!! Why?
#

Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.corpus import brown
>>> brown_adventure_tagged = brown.tagged_words(categories='adventure', simplify_tags=False)
>>> tag_fd = nltk.FreqDist(tag for (word, tag) in brown_adventure_tagged if tag.startswith('N'))
>>> tag_fd.keys()[:50]
['NN', 'NNS', 'NP', 'NN-TL', 'NP$', 'NN$', 'NR', 'NP-TL', 'NPS', 'NNS-TL', 'NNS$', 'NN$-TL', 'NP$-TL', 'NP+BEZ', 'NN+BEZ', 'NR-TL', 'NN-HL', 'NN-NC', 'NPS$', 'NN+BEZ-TL', 'NN+HVZ', 'NN+HVZ-TL', 'NN+MD', 'NNS$-TL', 'NNS+MD', 'NP+MD', 'NR$', 'NR$-TL']
>>> 
