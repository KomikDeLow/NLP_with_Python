# fine

#presented by Iryna Tkachuk
#PRLc 13
#Identify words that can be plural nouns or third person singular verbs.

import nltk
import nltk.corpus

def get_nns_or_vbz_words():
    """ Returns a list of words, that are both tagged as NNS (plural nouns) and
    VBZ (3rd person singular verbs). """
    # Getting a full list of tagged words.
    all_words = nltk.corpus.brown.tagged_words()

    # Grabbing NNS-tagged words and filtering out duplicates.
    nns = set([word for word, tag in all_words if tag == 'NNS'])
    # Grabbing VBZ-tagged words and filtering out duplicates.
    vbz = set([word for word, tag in all_words if tag == 'VBZ'])

    # Calculating intersection of two sets (words tagged both as NNS and VBZ).
    words = nns.intersection(vbz)
    return list(words)
print '\nAmbiguous words tagged both as NNS (plural nouns) and VBZ (3rd person singular verbs):'
print get_nns_or_vbz_words()


