# TODO
# What proportion...?
# How many...? 
# What percentage...?
#

#Iryna Brykailo, ALs-13
#Chapter 5, Task 18

import nltk
from nltk.corpus import brown
brown_adventure_tagged = brown.tagged_words(categories='adventure', simplify_tags=True)
data = nltk.ConditionalFreqDist((word.lower(), tag)
                                for (word, tag) in brown_adventure_tagged)
for word in data.conditions():
    if len(data[word]) == 1:
        tags = data[word].keys()
        print word, ' '.join(tags)
        
#Розглядаю у корпусі Brown слова, яким відповідає один тег,
#тобто які є однозначними.

for word in data.conditions():
    if len(data[word]) > 2:
        tags = data[word].keys()
        print word, ' '.join(tags)

#Розглядаю у корпусі Brown слова, яким відповідає два і більше тегів,
#тобто які є багатозначними.
#Результат показав, що кількість багатозначних слів є значно більшою,
#ніж кількість однозначних.


