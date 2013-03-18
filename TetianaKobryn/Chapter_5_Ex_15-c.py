Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> import nltk
>>> from nltk.corpus import brown
>>> brown_adventure_tagged = brown.tagged_words(categories='adventure', simplify_tags=True)
>>> tag_fd = nltk.FreqDist(tag for (word, tag) in brown_adventure_tagged)
>>> tag_fd.keys()[:20]
['N', 'DET', 'PRO', 'P', '.', 'V', 'ADV', 'VD', ',', 'CNJ', 'ADJ', 'NP', 'VG', 'VN', '``', "''", 'WH', 'TO', 'MOD', 'NUM']
>>> 
