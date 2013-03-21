# Andrew Melnyk ALs-12

import nltk
from nltk.corpus import brown
words_brown=brown.tagged_words() 
tags_brown=[t for w,t in words_brown] # Присвоюю змінній теги корпусу Brown та роблю частотний аналіз
fd=nltk.FreqDist(tags_brown)
fd.items()[:10] 
