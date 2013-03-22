# TODO
# Lines should be less than 80 characters long
#

import nltk
from nltk.corpus import brown
sent1=nltk.word_tokenize("Go away!")
nltk.pos_tag(sent1)
#Hensirovska_Khrystyna.Коли я виконала токенізацію першого речення,то програма визначила,що слово GO  в реченні Go away! належить до частини мови іменник.Це непавильне визначення частини мови,бо слово GO є дієсловом.
sent2=nltk.word_tokenize("We went on the excursion.")
nltk.pos_tag(sent2)
#Виконавши токенізацію другого речення,отримуємо результат,що слово went є дієсловом минулого часу.
print nltk.pos_tag(sent1)
print nltk.pos_tag(sent2)
#Вивівши результати,можна зробити висновок,
#що слова go та went мають морфологічні відмінності,тому
#вони не можуть вільно змінюватися залежно від контексту.
#Так як кожна з цих форм залежить від граматичного контексту
#речення.
