# TODO
# I need Python modul.
#


#����������� ��������,����-12
#����� 8,�������� 8
#In the recursive descent parser demo, experiment with changing the sentence to
#be parsed by selecting Edit Text in the Edit menu.
import nltk
#������������ ������ ���������
grammar1 = nltk.parse_cfg("""
#S -> NP VP
#VP -> V NP | V NP PP
#PP -> P NP
#V -> "saw" | "ate" | "walked"
#NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
#Det -> "a" | "an" | "the" | "my"
#N -> "man" | "dog" | "cat" | "telescope" | "park"
#P -> "in" | "on" | "by" | "with"
#""")
rd_parser = nltk.RecursiveDescentParser(grammar1)#�������� ������������� ������
sent = 'Mary saw a dog'.split()#�������� �������
for t in rd_parser.nbest_parse(sent):
	print t #�������� �� ����� ������������ �����
sent = 'John ate a cat'.split() #������ �������

for t in rd_parser.nbest_parse(sent):
	print t #�������� �� ����� ������������ �����

sent = 'Bob saw a telescope'.split() #�������������� ��������� �� ���� �������
for t in rd_parser.nbest_parse(sent):
  print t

sent = 'Mary saw Bob with a cat'.split() #������� �������
for t in rd_parser.nbest_parse(sent):
	print t

sent = 'Mary saw Bob with a cat in the park'.split() #������ �� ������� ���
#�����
for t in rd_parser.nbest_parse(sent):
	print t
#����,������,�� recursive descent parser ���� ����� ������� �� ����� �������-
#����� �� ����������� ���� ���������,��� ���� ��������,�� ������ �����������-
#������ ��� ��������� ������.��������  ����� recursive descent parser � ������
#����������� �����,� ���� 䳺������.
