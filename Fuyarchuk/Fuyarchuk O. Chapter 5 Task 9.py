# fine

import nltk
from nltk.corpus import brown
text1 = nltk.word_tokenize("Go away!")
nltk.pos_tag(text1)
text2 = nltk.word_tokenize("We went on the excursion.")
nltk.pos_tag(text2)
print  nltk.pos_tag(text1)
print  nltk.pos_tag(text2)
#За допомогою морфологічного аналізатора pos_tag дана програма обробляє послідовність слів у реченні
#і ставить у відповідність до кожного з них відповідний тег.І дана програма показала, що слова GO and WENT не
#можна замінити одне на інше, бо цим словам відповідають різні теги.
