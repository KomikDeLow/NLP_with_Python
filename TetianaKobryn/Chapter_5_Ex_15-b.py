# TODO
# Comments?
# What does your program do?

import nltk
from nltk.corpus import brown
tagged_words = brown.tagged_words(categories='adventure', simplify_tags=False)
data = nltk.ConditionalFreqDist((word.lower(), tag)
                                    for (word, tag) in tagged_words)

for word in data.conditions():
        if len(data[word]) > 3:
            tags = data[word].keys()
            print word, ' '.join(tags)
