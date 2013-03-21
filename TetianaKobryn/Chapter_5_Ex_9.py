# Ex.9. Satisfy yourself that there are restrictions on the distribution of go and went, in
# the sense that they cannot be freely interchanged in the kinds of contexts illustrated
# in (3), Section 5.7.


# Forms 'go' and 'went' are morphologically distinct from one another.
# 'went' is only used in Past Simple tense and 'go' in Present Simple or is an infinitive.

import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='adventure', simplify_tags=True))
cfd['go'].keys()
# ['V']
cfd['went'].keys()
# ['VD']
