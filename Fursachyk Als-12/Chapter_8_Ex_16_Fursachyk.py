#Chapter_8_Ex_16_Fursachyk 
import nltk
entries = nltk.corpus.ppattach.attachments('training')# порожній словник за замовчуванням
table = nltk.defaultdict(lambda: nltk.defaultdict(set))# заповнення словника
for entry in entries:
	key = entry.noun1+ '-'+entry.prep +  '-' + entry.noun2 # пошук незмінної конструкції noun + preposition + noun
	if key =="noun1":
		key1 = entry.verb + '-' + entry.noun1 # конструкції noun + verb1
	elif key == "noun2":
		key1 = entry.verb + '-' + entry.noun2 # конструкції noun + verb2
	else:
		key1 = entry.verb + '-' + entry.prep
		
		pphrase = entry.noun1 + '-' + entry.prep +  '-' + entry.noun2
		table[key1][entry.attachment].add(pphrase)# список кортежів

		
print pphrase # виведення незмінної конструкції noun1+preposition+noun2 


