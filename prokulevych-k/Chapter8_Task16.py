# NameError: name 'entries' is not defined

#���������� �. ����-11, ����� 8, ������ 16
#Write a program to find those verbs in the PP Attachment Corpus nltk.corpus.ppattach.
#Find any cases where the same verb exhibits two different attachments,
#but where the first noun, or second noun, or preposition stays unchanged.
import nltk
table = nltk.defaultdict(lambda: nltk.defaultdict(set))#������ �������, ���������� ������ ����� ������ ��������
#���������� �������� �� ������� �� ������ ������ �������1-����������-�������1
# �� ��������� key ����� �������� ������ �������� �������� (�� ������ ���������,  #������������, ������ ���������)
for entry in entries:
	key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
	if key=="noun1":
		key1 = entry.verb + '-' + entry.noun1
	elif key=="noun2":
		key1 = entry.verb + '-' + entry.noun2
	else:
		key1 = entry.verb + '-' + entry.prep
pphrase = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
table[key1][entry.attachment].add(pphrase)#��������� �������� - ������ �������� - ������� � ������� V ��� N �� ����������  
print pphrase
