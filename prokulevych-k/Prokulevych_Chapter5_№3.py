#Прокулевич К, ПРЛс-11, Задача №3, Розділ5
# TODO
# Comments ?
# What  different  pronunciations  and  parts-of-speech  are involved?
#
# "присвоює кожному слову тег частину мови" what is it mean?
# "якою частиною мови виступає слово в реченні" ??
# Bad style (modul name, string (line) lenght)

import nltk
text = nltk.word_tokenize("They wind back the clock, while we chase after the wind.")
nltk.pos_tag(text)
print nltk.pos_tag(text)
# POS tagger опрацьовує послідовність слів і присвоює кожному слову тег частину мови. Результати програми показали, що слово 'They' - займенник, 'wind'-дієслово, 'back'-прислівник, 'the'-артикль, 'clock'-годинник, 'while'-сполучник, 'we'-займенник, 'chase'-дієслово, 'after'-сполучник, 'the'-артикль, 'wind'- іменник.   
#тобто POS tagger визначає якою частиною мови виступає слово в реченні. наприклад слово wind зусрічається 2 рази, перший раз воно виступає дієсловом, а другий-іменником.
