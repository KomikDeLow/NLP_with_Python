# TODO
# Comments?
# What does your program do?
# simplify_tag set doesn't use 

import nltk
from nltk.corpus import brown
brown_adventure_tagged = brown.tagged_words(categories='adventure', simplify_tags=False)
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_adventure_tagged)
print tag_fd.keys()[:20]
