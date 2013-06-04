# TODO
# Are  prepositional phrases in Brown
# What does PP consist? 
# Look nltk.help.brown_tagset()

#presented by Iryna Tkachuk
#PRLc 13
#Identify three-word prepositional phrases of the form IN + DET + NN

import nltk
import nltk.corpus

def identify_prepositional_phrases():
    """ Returns a list of three-word prepositional phrases in the form IN+DET+NN
    found in Brown Corpus. """
    phrases = []
    # Looping over all tagged sentences in Brown Corpus.
    for sentence in nltk.corpus.brown.tagged_sents(simplify_tags=True):
        # Generating all possible trigrams for each sentence.
        for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
            # Checking word tags in each trigram.
            if t1 == 'IN' and t2 == 'DET' and t3 == 'NN':
                # Condition satisfied. Joining words and saving in one list.
                ph = ' '.join([w1, w2, w3])
                phrases.append(ph)

    return phrases
print '\nPrepositional phrases matching \'IN+DET+NN\' pattern in Brown Corpus:'
print identify_prepositional_phrases()
