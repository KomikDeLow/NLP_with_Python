# NameError: name 'entries' is not defined

#Прокулевич К. ПРЛс-11, Розділ 8, Задача 16
#Write a program to find those verbs in the PP Attachment Corpus nltk.corpus.ppattach.
#Find any cases where the same verb exhibits two different attachments,
#but where the first noun, or second noun, or preposition stays unchanged.
import nltk
table = nltk.defaultdict(lambda: nltk.defaultdict(set))#пустий словник, значеннями записів якого будуть словники
#заповнення словника за ключами які будуть містити іменник1-прийменник-іменник1
# за допомогою key можна вибирати варіант побудови словника (за першим іменником,  #прийменником, другим іменником)
for entry in entries:
	key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
	if key=="noun1":
		key1 = entry.verb + '-' + entry.noun1
	elif key=="noun2":
		key1 = entry.verb + '-' + entry.noun2
	else:
		key1 = entry.verb + '-' + entry.prep
pphrase = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
table[key1][entry.attachment].add(pphrase)#аповнення словника - записи словника - словник з ключами V або N та значеннями  
print pphrase
