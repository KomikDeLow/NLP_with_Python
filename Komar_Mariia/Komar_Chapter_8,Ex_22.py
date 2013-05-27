# a приклади
# Певні дієслова вимагають певних прийменників, також і іменники
# TODO
# а як вливають ці конкретні дієслова та іменники
# 


#Komar Mariia Als-11
#Chapter_8, Ex_22

#Inspect the PP Attachment Corpus and try to suggest some factors
#that influence PP attachment.


import nltk
entries = nltk.corpus.ppattach.attachments('training') #працюємо з корпусом PP Attachments
table = nltk.defaultdict(lambda: nltk.defaultdict(set))
for entry in entries:
	key = entry.verb + '-P-' + entry.noun1 #створюємо фрази з якими будемо працювати 
	table[key][entry.attachment].add(entry.prep)

for key in sorted(table): 
	if len(table[key]) > 1: #створюємо умову для презинтабельного виводу 
		print key, '-', 'P depends on N:', sorted(table[key]['N']), 'P depends on V:', sorted(table[key]['V'])

#після виводу на екран, ми бачимо спочатку фразу,
#потім усі прийменники, які можна використовувати
#після даного дієслова і перед даним іменником
#Тобто на місце приєднання PP впливають конкретні дієслова та іменники 
		

