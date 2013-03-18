# Forms 'go' and 'went' are morphologically distinct from one another.
# 'went' is only used in Past Simple tense and 'go' in Present Simple or is an infinitive.

>>> cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='adventure', simplify_tags=True))
>>> cfd['go'].keys()
['V']
>>> cfd['went'].keys()
['VD']
