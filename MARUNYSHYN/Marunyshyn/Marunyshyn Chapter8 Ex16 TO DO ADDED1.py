#Irena Marunyshyn PRLs-12 Chapter 8 Ex 16 Write a program to find those verbs in the PP Attachment Corpus nltk.cor
#pus.ppattach. Find any cases where the same verb exhibits two different at-
#tachments, but where  the  first noun, or  second noun, or preposition  stays
#unchanged (as we saw in our discussion of syntactic ambiguity in Section 8.2).
# rozvjazok zadachi
import nltk
entries = nltk.corpus.ppattach.attachments('training')# pustuj slovnuk po zamovchanny
table = nltk.defaultdict(lambda: nltk.defaultdict(set))# zapovnennja slovnuka
for entry in entries:
	key = entry.noun1+ '-'+entry.prep +  '-' + entry.noun2# looking for unchangeble construction noun + preposition + noun
	if key =="noun1":
		key1 = entry.verb + '-' + entry.noun1# noun + verb1
	elif key == "noun2":
		key1 = entry.verb + '-' + entry.noun2# noun + verb2
	else:
		key1 = entry.verb + '-' + entry.prep
		
		pphrase = entry.noun1 + '-' + entry.prep +  '-' + entry.noun2
		table[key1][entry.attachment].add(pphrase)# list of corteges

		
print pphrase # print noun1+preposition+noun2 = unchangeble construction
# with the help of this program we can find different groups of words which have construction Noun+ prepositon+ noun
# and also the words constraction which are unchangeble. also I find unchangeble construction as stance-in-light. 

