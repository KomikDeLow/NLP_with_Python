# TODO
# Comments?
# What does your program do?

#Presentd by Tetiana Kobryn
#
#Chapter 5, Ex.15d
#d. Which tags are nouns most commonly found after? What do these tags
#represent?

import nltk
from nltk.corpus import brown
#defining tagged words
brown_adventure_tagged = brown.tagged_words()
#creating a frequency distribution containing tags that start with "NN"
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_adventure_tagged if
                       tag.startswith('NN'))
#presenting a list of tags
print tag_fd.keys()[:10]

"""
for example
NN -> 'year', 'time'
NNS -> 'years', 'members'
NN$ -> "year's", "world's"
NN$-TL -> "President's", "University's"
NN-HL -> 'cut', 'Salary', 'condition'
NN-TL -> 'President', 'House', 'State'
NN-TL-HL -> 'Fort', 'City', 'House'
NNS$ -> "children's", "women's"
NNS-HL -> 'years', 'idols', 'Creations'
NNS-TL -> 'States', 'Nations'
NNS-TL-HL -> 'Nations'
"""
