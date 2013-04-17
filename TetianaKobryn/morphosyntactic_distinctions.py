# fine
#
#Presented by Tetiana Kobryn

#Chapter 5, Ex.9
# Satisfy yourself that there are restrictions on the distribution of go and went, in
# the sense that they cannot be freely interchanged in the kinds of contexts illustrated
# in (3), Section 5.7.


import nltk
from nltk.corpus import brown
#sorting brown adventure tagged words  by frequency
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='adventure',
                                                  simplify_tags=False))
#representing tags for given word
go_tag = cfd['go'].keys()
print "go", go_tag
went_tag = cfd['went'].keys()
print "went", went_tag

print """Forms 'go' and 'went' are morphologically distinct from one another.
Verb 'went' belongs to Past Simple category and 'go' to a base category."""
