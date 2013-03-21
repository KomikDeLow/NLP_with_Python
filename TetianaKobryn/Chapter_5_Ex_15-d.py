import nltk
from nltk.corpus import brown
brown_adventure_tagged = brown.tagged_words(categories='adventure', simplify_tags=False)
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_adventure_tagged if tag.startswith('N'))
print tag_fd.keys()[:50]

