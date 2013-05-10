# TODO
# Навіщо перші  два цикли? 
# Далі зовсім все заплутано  key =="noun1? Що це за змінна key?
# Функція find_verb є але не використовується. Чому?



#Irena Marunyshyn PRLs-12  Write a program to find those verbs in the PP Attachment Corpus nltk.cor
#pus.ppattach. Find any cases where the same verb exhibits two different at-
#tachments, but where  the  first noun, or  second noun, or preposition  stays
#unchanged (as we saw in our discussion of syntactic ambiguity in Section 8.2).
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
print pphrase# print noun1+preposition+noun2
# with the help of this program we can find different groups of words which have construction Noun+ prepositon+ noun
# and also the words constraction which are unchangeble. also I find unchangeble construction as stance-in-light. 
