# TODO
# Comments?
# Use full set of tags
#

import nltk
from nltk.corpus import brown
brown_tagged=brown.tagged_words(simplify_tags=True)
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_tagged)
sorted(set(tag_fd.keys()))
print sorted(set(tag_fd.keys()))
