
import nltk
import nltk.corpus
def get_nns_or_vbz_words():
    """ Returns a list of words, that are both tagged as NNS (plural nouns) and VBZ (3rd person singular verbs). """
    # getting a full list of taged words.
    all_words = nltk.corpus.brown.tagged_words()
    
    # grabbing NNS-tagged words and filtering out duplicates.
    nns = set([word for word, tag in all_words if tag == 'NNS'])

    # grabbing VZB-tagged words and filtering out duplicates.
    vbz = set([word for word, tag in all_words if tag == 'VBZ'])

    # calculating intersection of two sets (words tagged both as NNS and VZB).
    words = nns.intersection(vbz)
    return list(words)
print '\nAmbiguous words tagged both as NNS (plural nouns) and VBZ (3rd person singular verbs):'
print get_nns_or_vbz_words()
