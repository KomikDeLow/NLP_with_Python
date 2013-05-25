# Prizvuszcze / Grypa

import nltk
entries = nltk.corpus.ppattach.attachments('training')# pustuj slovnuk po zamovchanny
table = nltk.defaultdict(lambda: nltk.defaultdict(set))# zapovnennja slovnuka
for entry in entries:
	 key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2#  nuon+ preposiyion + noun
	 table[key][entry.attachment].add(entry.verb)

	 
for key in sorted(table): # we can see the dictionary
	if len(table[key]) > 1:
		print key, 'N:', sorted(table[key]['N']), 'V:', sorted(table[key]['V'])# print dictionary

# rozvjazok zadachi
import nltk
entries = nltk.corpus.ppattach.attachments('training')## pustuj slovnuk po zamovchanny
table = nltk.defaultdict(lambda: nltk.defaultdict(set))# zapovnennja slovnuka
for entry in entries:
	if key =="noun1":
		key1 = entry.verb + '-' + entry.noun1# verb + noun
	elif key == "noun2":
		key1 = entry.verb + '-' + entry.noun2# verb + noun
	else:
		key1 = entry.verb + '-' + entry.prep# verb + preposition
		pphrase = entry.noun1 + '-' + entry.prep +  '-' + entry.noun2# noun + preposition + noun
		table[key1][entry.attachment].add(pphrase)# list of corteges

def find_verb(verb):
	 return [(verb,w1[i]) for i in w1.keys() if str(i).startswith(verb) and len(w1[i])>1] # result of any verbs
print pphrase
