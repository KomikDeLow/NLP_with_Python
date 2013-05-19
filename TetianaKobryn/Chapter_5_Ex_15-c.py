# TODO
# Comments?
# What does your program do?
# simplify_tag set doesn't use 

#Presented by Tetiana Kobryn
#
#Chapter 5, Ex.15c
#c. List tags in order of decreasing frequency. What do the 20 most frequent
#tags represent?

import nltk
from nltk.corpus import brown
#defining tagged words
brown_adventure_tagged = brown.tagged_words(categories='adventure',
                                            simplify_tags=False)
#creating a frequency distribution containing list of tags
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_adventure_tagged)
#presenting list of 20 tags in order of decreasing frequency
print tag_fd.keys()[:20]

