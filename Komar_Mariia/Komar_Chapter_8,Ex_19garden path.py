# bad programming style
# TODO
# � �� ��������� �� ���������� ������������ ��������� � �������� ������������ ����� ������ �garden path� �������
# �� "������� c����������� ����� ����� ������ ����� �� � ��� ������, ��� � ��� ��������" ������� ���������

#Komar Mariia Als-11
#Chapter_8, Ex_19

#Read up on �garden path� sentences. How might the computational work of
#a parser relate to the difficulty humans have with processing these sentences?
#(See http://en.wikipedia.org/wiki/Garden_path_sentence.)

import nltk
grammar = nltk.parse_cfg("""
S -> NP VP
NP -> Det N | Det N VP
VP -> V NP | V
Det -> 'The' | 'the'
N -> 'old' | 'boat'
V -> 'man'
""") # ��������� ���������
sent = ['The', 'old', 'man', 'the', 'boat'] # ��������� �������
parser = nltk.ChartParser(grammar) # ������������� ChartParser ��� ������ ������ 
trees = parser.nbest_parse(sent)
for tree in trees:
	print 'Tree = ', tree # �������� ������ �� �����
	

answer1=('_______________Answer:')
print answer1
answer=('#�garden path� sentences - �� ���������� �������� �������, � ���� ����� ����� �����, ����� �������� �� ������� c����������� ����� ����� ������ ����� �� � ��� ������, ��� � ��� ��������.���������  �The old man the boat.� �� ���� ��������, �� "������ ������ ... �����", ����� ������� ���������� ���� �� ��� 䳺�����,��� �������� "man" �� 䳺����� �� ������ "����������������" � �� ������� ������������ �� "������ ������������ �����". ����, �� � ������ ��� � ������ ���� ������������ �������,���� ������ ���������� ������ �������.')
print answer



#�garden path� sentences - �� ���������� �������� �������, � ���� ����� �����
#�����, ����� �������� �� ������� c����������� ����� ����� ������ �����
#�� � ��� ������, ��� � ��� ��������.��� ���� �� ��� 䳺�����,
#��� �������� "man" �� 䳺����� �� ������ "����������������" � �� �������
#������������ �� "������ ������������ �����". ����, �� � ������ ��� � ������
#���� ������������ �������,���� ������ ���������� ������ �������.
