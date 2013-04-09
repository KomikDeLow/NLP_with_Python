#Iryna Brykailo, ALs-13
#Chapter 5, Task 21

import nltk
from nltk.corpus import brown
fd = nltk.FreqDist()
text=nltk.corpus.brown.words(categories='adventure')
dic=['']
for (wd, tg) in nltk.corpus.brown.tagged_words():
            if tg[:2] == 'QL':
                fd.inc(wd)
                verbs=['adore', 'love', 'like', 'prefer']
                for i in range(len(text)):
                    if text[i]in fd.keys()and text[i+1]in verbs and (text[i]+' '+text[i+1]) not in dic:
                        dic.append(text[i]+' '+text[i+1])
                        print dic

#У результаті виконання програми ми отримуємо ряд специфікаторів,
#які найчастіше зустрічаються перед словами adore, love, like та prefer.
#Тaкож можна зробити висновок, що ці слова також можуть викорстовуватися
#не лише як дієслова, залежно від контексту.
