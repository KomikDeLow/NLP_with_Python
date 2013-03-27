#presented by Iryna Tkachuk PRLc 13
#Produce an alphabetically sorted list of the distinct words tagged as MD

import nltk
import nltk.corpus

def get_sorted_md_words():
    """ Returns a sorted list of distinct words tagged as MD. """
    # Getting a full list of tagged words.
    all_words = nltk.corpus.brown.tagged_words()

    # Each element of all_words is a tuple containing word and it's tag.
    # Getting a list of MD-tagged words only.
    md_words = [word for word, tag in all_words if tag == 'MD']

    # Converting md_words to set() to get only distinct elements and sorting it.
    md_words = sorted(set(md_words))

    return md_words

print '\nList of sorted words tagged as MD in Brown Corpus:'
print get_sorted_md_words()
