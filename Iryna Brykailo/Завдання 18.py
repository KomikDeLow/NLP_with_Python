# TODO
# Comments?
# What does your program do?
# What proportion?
# How many words?
# What percentage?
import nltk
from nltk.corpus import brown
brown_adventure_tagged = brown.tagged_words(categories='adventure', simplify_tags=True)
data = nltk.ConditionalFreqDist((word.lower(), tag)
                                for (word, tag) in brown_adventure_tagged)
for word in data.conditions():
    if len(data[word]) == 1:
        tags = data[word].keys()
        print word, ' '.join(tags)
for word in data.conditions():
    if len(data[word]) > 2:
        tags = data[word].keys()
        print word, ' '.join(tags)
