# TODO
# Your program doesn't have output
#

#Iryna Brykailo, Als-13
#Chapter 5, Task 3

import nltk
from nltk.corpus import brown
text = nltk.word_tokenize("They wind back the clock, while we chase after the wind")
nltk.pos_tag(text)
print nltk.pos_tag(text)

#Використовуючи функцію Pos tagger я здійснила розподіл речення на слова та теги,
#які вказують на частини мови.
#У результаті я помітила, що в даному реченні вживається двічі слово wind.
#але у обох випадках воно позначає різні частини мови.
#У першому - це дієслово, у другому - іменник.
#Отже, можна зробити висновок, що слова із однаковим написанням
#можуть мати різне значення та інколи різний звуковий склад, залежно від контексту.


