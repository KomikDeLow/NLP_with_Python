#presented by Iryna Tkachuk
#PRLc 13
#calculate_pronoun_ratio()

import nltk
from nltk.corpus import brown

MALE_PRONOUNS = ['he','his','him','himself', 'he\'s','he\'d','he\'ll']
FEMALE_PRONOUNS = ['she','hers','her','herself', 'she\'s','she\'d','she\'ll']
PRONOUN_TAGS = ['PP$$','PPL','PPO','PPS','PPS+BEZ','PPS+HVD','PPS+HVZ','PPS+MD']

def calculate_pronoun_ratio():
    """ Calculates ratio of masculine to feminine pronouns in brown corpus. """
    # Get a full list of tagged words in Brown Corpus. Conver words to lowercase.
    words = [(word.lower(), tag) for word, tag in nltk.corpus.brown.tagged_words()]

    # Build a ConditionalFreqDist object.
    cfd = nltk.ConditionalFreqDist(words)

    # Find number of male/female pronoun occurences.
    mp_count = sum([cfd[p][t] for t in PRONOUN_TAGS for p in MALE_PRONOUNS])
    fp_count = sum([cfd[p][t] for t in PRONOUN_TAGS for p in FEMALE_PRONOUNS])

    # Get ratio.
    ratio = float(mp_count) / float(fp_count) * 0.1

    return ratio
print '\nRatio of male pronouns to female pronouns in Brown Corpus:'
print calculate_pronoun_ratio()

