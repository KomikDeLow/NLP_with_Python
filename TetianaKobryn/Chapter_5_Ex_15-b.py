# TODO
# Comments?
# What does your program do?

#Presented by Tetiana Kobryn
#
#Chapter 5, Ex.15b
#b. Which word has the greatest number of distinct tags? What are they, and what
#do they represent?

import nltk
from nltk.corpus import brown
#defining tagged words
tagged_words = brown.tagged_words(categories='adventure', simplify_tags=False)
#creating conditional frequency distribution from a list of words and tags
data = nltk.ConditionalFreqDist((word.lower(), tag)
                                    for (word, tag) in tagged_words)
#presenting list of words, which have more than 3 tags
for word in data.conditions():
        if len(data[word]) > 3:
            tags = data[word].keys()
            print word, ' '.join(tags)
