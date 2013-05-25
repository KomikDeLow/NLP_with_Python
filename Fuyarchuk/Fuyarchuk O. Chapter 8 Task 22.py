# Fuyarchuk O. Chapter 8 Task 22
#Правила за якими здійснюється пошук всіх випадків вживання дієслова з двома різними
# PP, в яких перший або другий іменник, або прийменник залишається незмінним 
import nltk
entries = nltk.corpus.ppattach.attachments('training') 
table = nltk.defaultdict(lambda: nltk.defaultdict(set)) 
for entry in entries:
	key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
	table[key][entry.attachment].add(entry.verb)

for key in sorted(table): 
	if len(table[key]) > 1:
		print key, 'N:', 'N depends on V:', sorted(table[key]['N']), 'V:', sorted(table[key]['V'])
		
