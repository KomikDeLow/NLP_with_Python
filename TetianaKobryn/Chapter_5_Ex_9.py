
# Дієслівні форми "go" і "went" не можна замінити одна одною, 1-ша відповідає теперішньому часу, а 2-га - минулому.

>>> cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='adventure', simplify_tags=True))
>>> cfd['go'].keys()
['V']
>>> cfd['went'].keys()
['VD']
