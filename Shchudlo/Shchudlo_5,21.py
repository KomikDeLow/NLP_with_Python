#TODO
#love and like are a noun too
import nltk
from nltk.corpus import brown
bigram_list=nltk.bigrams(brown.tagged_words())
bigrams_QL=[w for w in bigram_list if w[0][1].startswith('QL')]
word_list=['adore','love','like','prefer']
bigrams_with_needed_words=[w for w in bigrams_QL if w[1][0].lower() in word_list]
list_QL=[w[0][0] for w in bigrams_with_needed_words]
print set(list_QL)

