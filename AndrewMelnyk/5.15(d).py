# TODO
# Program doesn't have output

# Andrew Melnyk ALs-12

import nltk
from nltk.corpus import brown
taggedw=brown.tagged_words() # Зі слів корпусу Brown відбираємо ті у яких теги починаються з NN і робимо частотний аналіз
tags=[t for w,t in taggedw if t.startswith('NN')] 
fd=nltk.FreqDist(tags)
print fd.items()[10:]

